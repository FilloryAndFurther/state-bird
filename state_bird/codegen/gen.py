import click
from .variables import write_state_rows, write_event_rows
from .ladder import generate_event_lines
import state_bird.data.read


@click.group()
def gen_main_group():
    pass


@click.command()
@click.option('--module-name', '-m', default='all')
def generate_var_csv(module_name):
    if module_name == 'all':
        modules = state_bird.data.read.get_all_modules()
        for module in modules:
            write_state_rows(module[1])
            write_event_rows(module[1])
    else:
        write_state_rows(module_name)
        write_event_rows(module_name)


@click.command()
@click.option('--module-name', '-m', default='all')
def generate_ladder(module_name):
    generate_event_lines(module_name)


gen_main_group.add_command(generate_var_csv)
gen_main_group.add_command(generate_ladder)

if __name__ == '__main__':
    gen_main_group()
