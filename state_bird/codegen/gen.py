import click

from .commands import (
    generate_var_csv,
    generate_ladder
)


@click.group()
def gen_main_group():
    pass


gen_main_group.add_command(generate_var_csv)
gen_main_group.add_command(generate_ladder)

if __name__ == '__main__':
    gen_main_group()
