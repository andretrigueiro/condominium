"""
Contains the application factory function.
Configure the flask app, register the blueprints, set the CORS and add command line commands
"""

from flask import Flask, jsonify
from flask_cors import CORS

# Import command line commands
from api.db.config_db import init_app

# Factory function
def create_app():

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True, static_url_path='', static_folder='../client/public/')
    app.config.from_object(__name__)
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY='dev',
    )

    # enable CORS
    CORS(app, supports_credentials=True, resources={r'/*': {'origins': '*'}})

    # sanity check route
    @app.route('/ping', methods=['GET'])
    def ping_pong():
        return jsonify('pong!')

    # Register DB commands
    init_app(app)

    # Register blueprints and add it to CORS
    from . import auth
    app.register_blueprint(auth.bp)
    CORS(auth.bp)

    from . import houses
    app.register_blueprint(houses.bp)
    CORS(houses.bp)

    from . import users
    app.register_blueprint(users.bp)
    CORS(users.bp)

    return app