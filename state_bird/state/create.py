import state_bird.data.write as write
import state_bird.data.create
import state_bird.data.read


def create_event(name, from_state, to_state):
    current_id = state_bird.data.read.get_current_module(get_id=True)
    if state_bird.data.read.state_exists(from_state, current_id) and state_bird.data.read.state_exists(to_state, current_id):
        state_bird.data.create.add_event(name, from_state, to_state, current_id)
        return True
    else:
        return False


def copy_module(module_name, new_name):
    """ Copies a module and all of its states and events """
    states = state_bird.data.read.get_states_by_module_name(module_name)
    events = state_bird.data.read.get_events_by_module_name(module_name)
    state_bird.data.create.create_module(new_name)
    write.set_current_module(new_name)
    for state in states:
        state_bird.data.create.add_state(state[2], state[3])
    for event in events:
        state_bird.data.create.add_event(event[2], event[3], event[4], event[5])
    return True
