# File that contains the functions to read the data from the database
# Path: app/data/read.py

import sqlite3
import json

# Create a function that returns all the states from the states table
def get_states():
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM states")
    states = cur.fetchall()
    con.close()
    return states


# Create a function that returns all the events from the events table
def get_events():
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
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

# Function that returns the current module from config.json
def get_current_module():
    with open('state_bird/data/config.json', 'r') as f:
        config = json.load(f)
        return config['current_module']