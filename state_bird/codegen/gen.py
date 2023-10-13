import click
from .variables import create_state_rows, write_state_rows


@click.group()
def gen_main_group():
    pass


@click.command()
def generate_var_csv():
    write_state_rows('lgvol')


gen_main_group.add_command(generate_var_csv)

if __name__ == '__main__':
    gen_main_group()
