import click

import state_bird.data.create
import state_bird.data.read
import state_bird.data.write
import state_bird.data.update


@click.command()
def add_input():
    name = click.prompt("Input name")
    slot = click.prompt("Input slot")
    state_bird.data.create.create_input(name, slot)


@click.command()
def add_output():
    name = click.prompt("Output name")
    slot = click.prompt("Output slot")
    state_bird.data.create.create_output(name, slot)


@click.command()
@click.argument('name')
def set_project_name(name):
    state_bird.write.set_current_project(name)
