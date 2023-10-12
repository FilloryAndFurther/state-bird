import json

# function that writes to current_module in config.json to argument
def set_current_module(module_name):
    with open('state_bird/data/config.json', 'r') as f:
        config = json.load(f)
        config['current_module'] = module_name
    with open('state_bird/data/config.json', 'w') as f:
        json.dump(config, f)

