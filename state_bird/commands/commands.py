import click
from state_bird.data.initdb import init_db, clear_db
import state_bird.data.create as create
import state_bird.data.read
import state_bird.data.write
import state_bird.state.create
import state_bird.state.graph as graph

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
@click.option('--name', '-n', multiple=True, help='The module(s) to add the state to')
def add_state(name):
    for n in name:
        create.add_state(n)
        click.echo("Added state {}".format(n))


@click.command()
@click.argument('module_name')
def set_current_module(module_name):
    if state_bird.data.read.module_exists(module_name):
        state_bird.data.write.set_current_module(module_name)
        click.echo(f"Current module set to {module_name}")
    else:
        click.echo(f"Module {module_name} does not exist")

# Command that gets all of the states and prints them out
@click.command()
@click.option('--current / --all', default=False, help='Get the current state or all states')
def get_states(current):
    states = state_bird.data.read.get_states()
    current_module_id = state_bird.data.read.get_current_module(get_id=True)
    for state in states:
        if current:
            if state[1] == current_module_id:
                click.echo(state)
        else:            
            click.echo(state)

@click.command()
def get_events():
    events = state_bird.data.read.get_events()
    for event in events:
        click.echo(event)

# Command that adds an event to the database
@click.command()
@click.argument('name')
@click.argument('from_state')
@click.argument('to_state')
def add_event(name, from_state, to_state):
    res = state_bird.state.create.create_event(name, from_state, to_state)
    if res:
        click.echo(f"Added event {name} from {from_state} to {to_state}")
    else:
        click.echo(f"State {from_state} or {to_state} does not exist")
        
        
# Command that displays a graph of the current module
@click.command()
def show_graph():
    graph.get_graph()