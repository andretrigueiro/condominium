"""
Control Database commands.
The only one in use to tests is "populate-db"
"""

import click
from flask import g
from flask.cli import with_appcontext
from api.db.mongodb import DATABASE
from api.db.mongodb.users_db import set_initial_onwer
from api.db.userdata import ADM, RESIDENT, HOUSES


# Associate the db with G element
def get_db():
    if 'db' not in g:
        g.db = DATABASE

    return g.db

# Command line to populate the DB with test data
@click.command('populate-db')
@with_appcontext
def populate_db_command():
    """Populate DB with data."""
    DATABASE.houses.insert_many(HOUSES)
    DATABASE.residents.insert_many(RESIDENT)
    DATABASE.adm.insert_many(ADM)
    set_initial_onwer()
    click.echo('Populated the database.')

# Initiate the database
def init_db():
    db = get_db()

# Command line to initiate the database
@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')

# Close database connection
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        DATABASE.close()

# Command line to close the database
@click.command('close-db')
@with_appcontext
def close_db_command():
    close_db()
    click.echo('Closed the database.')

# Function to register these functions
def init_app(app):
    app.cli.add_command(init_db_command)
    app.cli.add_command(populate_db_command)
    app.cli.add_command(close_db_command)