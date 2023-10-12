import click
from state_bird.commands.commands import init, clear, create_module, add_state, set_current_module, get_states, add_event, show_graph

@click.group()
def main():
    pass
main.add_command(clear)
main.add_command(init)
main.add_command(create_module)
main.add_command(add_state)
main.add_command(set_current_module)
main.add_command(get_states)
main.add_command(add_event)
main.add_command(show_graph)

if __name__ == '__main__':
    main.add_command(clear)
    main.add_command(init)
    main.add_command(create_module)
    main.add_command(add_state)
    main.add_command(set_current_module)
    main.add_command(get_states)
    main.add_command(add_event)
    main.add_command(show_graph)
    main()