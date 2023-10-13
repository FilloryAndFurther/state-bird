import os
from pathlib import Path
from state_bird.data.read import (
    get_states_by_module_name,
    get_events_by_module_name,
)


def create_state_rows(module_name):
    """
    Creates a list of strings that represent the rows of the state table.
    {module}_state is a DINT while {module}_s{n} is a BOOL alias for bits
    within the DINT.
    """
    rows = []
    # Initial dint
    main_string = f'{module_name}_state,DINT,,,,Var,ReadWrite,,,False'
    rows.append(main_string)
    # Bool aliases
    states = get_states_by_module_name(module_name)
    for i, state in enumerate(states):
        alias_string = f'{module_name}_s{i+1},BOOL,,,,Var,ReadWrite,{state[2]},{module_name}_state.{state[3]},False'
        rows.append(alias_string)
    return rows


def write_state_rows(module_name):
    """
    Writes the rows of the state table to a csv file in a documents folder.
    """
    documents_folder = Path(os.path.expanduser("~/Documents"))
    folder_path = documents_folder / 'state_bird_storage'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_name = f'{module_name}_var.csv'
    file_path = documents_folder / 'state_bird_storage' / file_name
    rows = create_state_rows(module_name)
    with open(file_path, 'a') as f:
        for row in rows:
            f.write(row + '\n')
    return True


def create_event_rows(module_name):
    """
    Creates a list of strings that represent the rows of the event table.
    """
    rows = []
    main_string = f'{module_name}_events,DINT,,,,Var,ReadWrite,,,False'
    rows.append(main_string)
    events = get_events_by_module_name(module_name)
    for i, event in enumerate(events):
        event_string = f'{module_name}_e{i+1},BOOL,,,,Var,ReadWrite,{event[2]},{module_name}_event.{event[5]},False'
        rows.append(event_string)
    return rows


def write_event_rows(module_name):
    """
    Writes the rows of the event table to a csv file in a documents folder.
    """
    documents_folder = Path(os.path.expanduser("~/Documents"))
    folder_path = documents_folder / 'state_bird_storage'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_name = f'{module_name}_var.csv'
    file_path = documents_folder / 'state_bird_storage' / file_name
    rows = create_event_rows(module_name)
    with open(file_path, 'a') as f:
        for row in rows:
            f.write(row + '\n')
    return True
