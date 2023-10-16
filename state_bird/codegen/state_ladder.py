import os
from pathlib import Path

from state_bird.data.read import get_events_by_module_name, get_state_by_name


def generate_event_line_strings(module_name):
    events = get_events_by_module_name(module_name)
    lines = []
    for i, event in enumerate(sorted(events, key=lambda x: x[5])):
        s = f'AFI OTE {module_name}_e{i+1}'
        lines.append(s)
    print(lines)
    return lines


def write_event_lines(module_name):
    """
    Writes event ladder lines to a file in the state_bird_storage folder.

    Args:
        module_name (str): The name of the module.

    Returns:
        None
    """
    lines = generate_event_line_strings(module_name)
    documents_folder = Path(os.path.expanduser("~/Documents"))
    folder_path = documents_folder / 'state_bird_storage'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_name = f'{module_name}_ladder.txt'
    file_path = documents_folder / 'state_bird_storage' / file_name
    with open(file_path, 'a') as f:
        for line in lines:
            f.write(line + '\n')


def generate_event_lines(module_name):
    write_event_lines(module_name)
    return True


def generate_state_transition_line_strings(module_name):
    events = get_events_by_module_name(module_name)
    lines = []
    for event in events:
        from_state = get_state_by_name(event[3])
        to_state = get_state_by_name(event[4])
        from_state_bit = from_state[3]
        to_state_bit = to_state[3]
        s = (
            f"XIC {module_name}_s{from_state_bit} XIC {module_name}_ons BST "
            f"MOV 0 {module_name}_state NXB OTS {module_name}_s{to_state_bit} BND"
        )
        lines.append(s)
    return lines


def write_state_transition_lines(module_name):
    lines = generate_state_transition_line_strings(module_name)
    documents_folder = Path(os.path.expanduser("~/Documents"))
    folder_path = documents_folder / 'state_bird_storage'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_name = f'{module_name}_ladder.txt'
    file_path = documents_folder / 'state_bird_storage' / file_name
    with open(file_path, 'a') as f:
        for line in lines:
            f.write(line + '\n')


def generate_state_transition_lines(module_name):
    write_state_transition_lines(module_name)
    return True
