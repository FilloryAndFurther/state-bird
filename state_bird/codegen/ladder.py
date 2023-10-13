from state_bird.data.read import get_events_by_module_name


def generate_event_lines(module_name):
    events = get_events_by_module_name(module_name)
    lines = []
    for i, event in enumerate(events):
        s = f'AFI OTE {module_name}_e{i+1}'
        lines.append(s)
    return lines


def generate_state_transition_lines(module_name):
    events = get_events_by_module_name(module_name)
    lines = []
