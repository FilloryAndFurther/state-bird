import click
from state_bird.data.initdb import init_db, clear_db
import state_bird.data.create as create
import state_bird.data.read
import state_bird.data.write
import json

@click.command()
def init():
    click.echo("Initializing the database...")
    init_db()
    click.echo("Initialized the database")
    
# Command that clears the database
@click.command()
def clear():
    click.confirm('Are you sure you want to clear the database?', abort=True)
    clear_db()
    click.echo('Database cleared')

# Command that creates a module
@click.command()
@click.argument('name')
def create_module(name):
    create.create_module(name)
    click.echo("Created module {}".format(name))

@click.command()
@click.argument('name')
def add_state(name):
    create.add_state(name)
    click.echo("Added state {}".format(name))


@click.command()
@click.argument('module_name')
def set_current_module(module_name):
    if state_bird.data.read.module_exists(module_name):
        state_bird.data.write.set_current_module(module_name)
        click.echo(f"Current module set to {module_name}")
    else:
        click.echo(f"Module {module_name} does not exist")