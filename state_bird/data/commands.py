import click
from .initdb import init_db


@click.command()
def init():
    click.echo("Initializing the database...")
    init_db()
    click.echo("Initialized the database")