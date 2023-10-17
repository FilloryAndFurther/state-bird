import click

from .commands import (
    generate_var_csv,
    generate_ladder,
    generate_input_ladder,
    generate_input_variables,
    generate_faults
)


@click.group()
def gen_main_group():
    pass


gen_main_group.add_command(generate_var_csv)
gen_main_group.add_command(generate_ladder)
gen_main_group.add_command(generate_input_ladder)
gen_main_group.add_command(generate_input_variables)
gen_main_group.add_command(generate_faults)

if __name__ == '__main__':
    gen_main_group()
