import click

from state_bird.commands.state_commands import (
    init,
    clear,
    create_module,
    add_state,
    set_current_module,
    get_states,
    add_event,
    show_graph,
    list_modules,
    delete_event,
    delete_state,
    copy_module
)

from state_bird.commands.controller_commands import (
    add_input,
    add_output,
    set_project_name
)


@click.group()
def controller():
    pass


@click.group()
def state():
    pass


state.add_command(clear)
state.add_command(init)
state.add_command(create_module)
state.add_command(add_state)
state.add_command(set_current_module)
state.add_command(get_states)
state.add_command(add_event)
state.add_command(show_graph)
state.add_command(list_modules)
state.add_command(delete_event)
state.add_command(delete_state)
state.add_command(copy_module)

controller.add_command(add_input)
controller.add_command(add_output)
controller.add_command(set_project_name)

if __name__ == '__main__':
    state.add_command(clear)
    state.add_command(init)
    state.add_command(create_module)
    state.add_command(add_state)
    state.add_command(set_current_module)
    state.add_command(get_states)
    state.add_command(add_event)
    state.add_command(show_graph)
    state()
