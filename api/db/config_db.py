import click
from flask import g
from flask.cli import with_appcontext
from api.db.mongodb import DATABASE
from api.db.userdata import ADM, RESIDENT, HOUSES

# Command line to populate the DB with test users
@click.command('test-db')
@with_appcontext
def test_db_command():
    """Populate DB with data."""
    selected_house = { "number": 2 }
    new_onwer = { "$set": { "onwer": "621f788affa87cb9f5139984" } }
    DATABASE.houses.update_one(selected_house, new_onwer)
    click.echo('Add onwer to house.')

# Associate the db with G element
def get_db():
    if 'db' not in g:
        g.db = DATABASE

    return g.db

# Command line to populate the DB with test users
@click.command('populate-db')
@with_appcontext
def populate_db_command():
    """Populate DB with data."""
    adms = DATABASE.adm
    adms.insert_many(ADM)
    residents = DATABASE.residents
    residents.insert_many(RESIDENT)
    houses = DATABASE.houses
    houses.insert_many(HOUSES)
    click.echo('Populated the database.')

# Initiate the database
def init_db():
    db = get_db()

# Command line to initiate the database
@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data."""
    init_db()
    click.echo('Initialized the database.')

# Close the G element
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        DATABASE.close()

# Command line to initiate the database
@click.command('close-db')
@with_appcontext
def close_db_command():
    """Clear the existing data and create new tables."""
    close_db()
    click.echo('Closed the database.')

# Function to register these functions
def init_app(app):
    app.cli.add_command(init_db_command)
    app.cli.add_command(populate_db_command)
    app.cli.add_command(close_db_command)
    app.cli.add_command(test_db_command)