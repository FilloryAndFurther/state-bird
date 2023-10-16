import shutil
from state_bird.data.read import (
    get_states_by_module_name,
    get_events_by_module_name,
)
from state_bird.util.file_util import generate_file_path


def create_state_rows(module_name):
    """
    Creates a list of strings that represent the rows of the state table.
    {module}_state is a DINT while {module}_s{n} is a BOOL alias for bits
    within the DINT.
    """
    rows = []
    main_string = f'{module_name}_state,DINT,,,,Var,ReadWrite,,,False'
    rows.append(main_string)
    ons_string = (
        f'{module_name}_ons,BOOL,,,,Var,ReadWrite,'
        f'oneshot,{module_name}_state.0,False'
    )
    rows.append(ons_string)
    states = get_states_by_module_name(module_name)
    for i, state in enumerate(states):
        alias_string = (
            f'{module_name}_s{state[3]},BOOL,,,,Var,ReadWrite,'
            f'{state[2]},{module_name}_state.{state[3]},False'
        )
        rows.append(alias_string)
    return rows


def write_state_rows(module_name):
    """
    Writes the rows of the state table to a csv file in a documents folder.
    """
    file_path = generate_file_path(f"{module_name}_var", 'csv')
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
        event_string = (
            f'{module_name}_e{event[5]},BOOL,,,,Var,ReadWrite,'
            f'{event[2]},{module_name}_event.{event[5]},False'
        )
        rows.append(event_string)
    return rows


def write_event_rows(module_name):
    """
    Writes the rows of the event table to a csv file in a documents folder.
    """
    file_path = generate_file_path(f"{module_name}_var", 'csv')
    rows = create_event_rows(module_name)
    with open(file_path, 'a') as f:
        for row in rows:
            f.write(row + '\n')
    return True


def copy_csv_template(module_name):
    """
    Copies the csv template to the documents folder.
    """
    path = generate_file_path(f"{module_name}_var", 'csv')
    shutil.copy('state_bird/codegen/ccw_variable_template.csv', path)
    return True
