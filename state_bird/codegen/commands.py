import click

from .state_variables import (
    write_state_rows,
    write_event_rows,
    copy_csv_template
)
from .state_ladder import (
    generate_event_lines,
    generate_state_transition_lines
)

import state_bird.data.read


@click.command()
@click.option('--module-name', '-m', default='all')
def generate_var_csv(module_name):
    if module_name == 'all':
        modules = state_bird.data.read.get_all_modules()
        for module in modules:
            write_state_rows(module[1])
            write_event_rows(module[1])
    else:
        copy_csv_template(module_name)
        write_state_rows(module_name)
        write_event_rows(module_name)


@click.command()
@click.option('--module-name', '-m', default='all')
def generate_ladder(module_name):
    generate_event_lines(module_name)
    generate_state_transition_lines(module_name)
