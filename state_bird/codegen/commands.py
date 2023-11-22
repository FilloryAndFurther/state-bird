import click

from .state_variables import (
    write_state_rows,
    write_event_rows,
    write_command_rows,
    copy_csv_template
)
from .state_ladder import (
    generate_event_lines,
    generate_state_transition_lines,
    generate_state_action_lines
)

from .io import write_io_lines, write_input_variables
from .faults import auto_create_verify_faults
import state_bird.data.read


@click.command()
@click.option('--module-name', '-m', default='all')
def generate_var_csv(module_name):
    if module_name == 'all':
        modules = state_bird.data.read.get_all_modules()
        # copy_csv_template("module_var")
        for module in modules:
            copy_csv_template(module[1])
            write_state_rows(module[1])
            write_event_rows(module[1])
            write_command_rows(module[1])
    else:
        copy_csv_template(module_name)
        write_state_rows(module_name)
        write_event_rows(module_name)
        write_command_rows(module_name)


@click.command()
@click.option('--module-name', '-m', default='all')
def generate_ladder(module_name):
    if module_name == 'all':
        modules = state_bird.data.read.get_all_modules()
        for module in modules:
            generate_event_lines(module[1])
            generate_state_transition_lines(module[1])
    else:
        generate_event_lines(module_name)
        generate_state_transition_lines(module_name)


@click.command()
def generate_input_variables():
    write_input_variables()


@click.command()
def generate_input_ladder():
    write_io_lines()


@click.command()
def generate_faults():
    auto_create_verify_faults()
    click.echo('Faults generated')


@click.command()
def generate_all():
    modules = state_bird.data.read.get_all_modules()
    for module in modules:
        copy_csv_template(module[1])
        write_state_rows(module[1])
        write_event_rows(module[1])
        write_command_rows(module[1])
    for module in modules:
        generate_event_lines(module[1])
        generate_state_transition_lines(module[1])
        generate_state_action_lines(module[1])
    write_input_variables()
    write_io_lines()
    auto_create_verify_faults()
    click.echo('All generated')
