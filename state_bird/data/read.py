# File that contains the functions to read the data from the database
# Path: app/data/read.py

import sqlite3
import json

# Create a function that returns all the states from the states table
def get_states(current_module = True):
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    if current_module:
        current_module = get_current_module(get_id=True)
        cur.execute("SELECT * FROM states WHERE module_id=?", (current_module,))
    else:
        cur.execute("SELECT * FROM states")
    states = cur.fetchall()
    con.close()
    return states


# Create a function that returns all the events from the events table
def get_events(current_module = True):
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    if current_module:
        current_module = get_current_module(get_id=True)
        cur.execute("SELECT * FROM events WHERE module_id=?", (current_module,))
    else:
        cur.execute("SELECT * FROM events")
    events = cur.fetchall()
    con.close()
    return events

# Function that checks if a module exists in the database
def module_exists(name):
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM modules WHERE name=?", (name,))
    module = cur.fetchone()
    con.close()
    if module:
        return True
    else:
        return False

# Function that gets module name from id
def get_module_name(module_id):
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    cur.execute("SELECT name FROM modules WHERE id=?", (module_id,))
    module_name = cur.fetchone()
    con.close()
    return module_name[0]

# Function that returns the current module from config.json
def get_current_module(get_id = False):
    with open('state_bird/data/config.json', 'r') as f:
        config = json.load(f)
        con = sqlite3.connect('state_bird/data/database.db')
        cur = con.cursor()
        if get_id:
            cur.execute("SELECT id FROM modules WHERE name=?", (config['current_module'],))
            module_id = cur.fetchone()
            con.close()
            return module_id[0]
        else:
            con.close()
        return config['current_module']

# Function that checks if a state exists within a module
def state_exists(name, module_id):
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE name=? AND module_id=?", (name, module_id))
    state = cur.fetchone()
    con.close()
    if state:
        return True
    else:
        return False