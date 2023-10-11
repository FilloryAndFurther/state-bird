import click
import state_bird.data.create as create


@click.command()
@click.argument('name')
def add_state(name):
    create.add_state(name)
    click.echo("Added state {}".format(name))