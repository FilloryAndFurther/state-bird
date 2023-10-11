import click
from state_bird.data.commands import init
from state_bird.state.create import add_state

@click.group()
def db_commands():
    pass

@click.group()
def main():
    pass

main.add_command(init)
main.add_command(add_state)

if __name__ == '__main__':
    main.add_command(init)
    main.add_command(add_state)
    main()