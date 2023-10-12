# Statebird

Allows you to create a simple state machine from the command line, and store in sqlite db. It can also display a simple graph of it.\
You can then generate simple structured text / ladder representing the state following [this example](https://control.com/technical-articles/state-machine-programming-in-ladder-logic-2/).

## Terminology

Module : high level object that you want to act as a state machine (valve, conveyor)\
event : edge from one state to another.

## How to use
Currently, to access the state creation interface, type \
`main`
to see a list of commands.

For any command, you can type the `--help` flag to see the options available. \
For example: `main create-event --help`\
Code generation commands can be seen under\
`gen`

## TODO

A lot.