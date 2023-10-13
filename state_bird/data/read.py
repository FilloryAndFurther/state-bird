# File that contains the functions to read the data from the database
# Path: app/data/read.py

import sqlite3
import json


def get_states(current_module=True):
    """
    Retrieve a list of all states and their associated data from the database.

    Args:
        current_module (bool): If True, only retrieve states associated with
        the current module.

    Returns:
        list: A list of tuples, where each tuple contains the data for a
        single state.
    """
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    if current_module:
        current_module = get_current_module(get_id=True)
        cur.execute("SELECT * FROM states WHERE module_id=?",
                    (current_module,))
    else:
        cur.execute("SELECT * FROM states")
    states = cur.fetchall()
    con.close()
    return states


def get_states_by_module_name(module_name):
    """
    Returns a list of all states that belong to a given module name.

    Args:
        module_name (str): The name of the module to retrieve states for.

    Returns:
        list: A list of tuples representing the states that belong to the
        given module.
    """
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE module_id IN (SELECT id FROM modules WHERE name=?)",
                (module_name,))
    states = cur.fetchall()
    con.close()
    return states


def get_events(current_module=True):
    """
    Retrieve events from the database.

    Args:
        current_module (bool): If True, retrieve events for the current module
        only.

    Returns:
        list: A list of tuples representing the events retrieved from the
        database.
    """
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    if current_module:
        current_module = get_current_module(get_id=True)
        cur.execute("SELECT * FROM events WHERE module_id=?",
                    (current_module,))
    else:
        cur.execute("SELECT * FROM events")
    events = cur.fetchall()
    con.close()
    return events


def module_exists(name):
    """
    Check if a module exists in the database.

    Args:
        name (str): The name of the module to check.

    Returns:
        bool: True if the module exists, False otherwise.
    """
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM modules WHERE name=?", (name,))
    module = cur.fetchone()
    con.close()
    if module:
        return True
    else:
        return False


def get_module_name(module_id):
    """
    Retrieve the name of a module from the database based on its ID.

    Args:
        module_id (int): The ID of the module to retrieve.

    Returns:
        str: The name of the module.
    """
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    cur.execute("SELECT name FROM modules WHERE id=?", (module_id,))
    module_name = cur.fetchone()
    con.close()
    return module_name[0]


def get_current_module(get_id=False):
    """
    Returns the current module name or ID from the config file and database.

    Args:
        get_id (bool): If True, returns the ID of the current module instead
        of its name.

    Returns:
        str or int: The name or ID of the current module.
    """
    with open('state_bird/data/config.json', 'r') as f:
        config = json.load(f)
        con = sqlite3.connect('state_bird/data/database.db')
        cur = con.cursor()
        if get_id:
            cur.execute("SELECT id FROM modules WHERE name=?",
                        (config['current_module'],))
            module_id = cur.fetchone()
            con.close()
            return module_id[0]
        else:
            con.close()
        return config['current_module']


def state_exists(name, module_id):
    """
    Check if a state exists in the database.

    Args:
        name (str): The name of the state to check.
        module_id (int): The ID of the module the state belongs to.

    Returns:
        bool: True if the state exists, False otherwise.
    """
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE name=? AND module_id=?",
                (name, module_id))
    state = cur.fetchone()
    con.close()
    if state:
        return True
    else:
        return False


def get_all_modules():
    """
    Retrieve all modules from the database.

    Returns:
        list: A list of tuples representing the modules retrieved from the
        database.
    """
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM modules")
    modules = cur.fetchall()
    con.close()
    return modules
