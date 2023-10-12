import state_bird.data.write
import state_bird.data.read

def create_event(name, from_state, to_state):
    current_id = state_bird.data.read.get_current_module(get_id=True)
    if state_bird.data.read.state_exists(from_state, current_id) and state_bird.data.read.state_exists(to_state, current_id):
        state_bird.data.create.add_event(name, from_state, to_state, current_id)
        return True
    else:
        return False