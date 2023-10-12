import sqlite3
import json
import state_bird.data.read as read

# Create a function that adds a state to the states table
def add_state(name):
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    # Get current_state from config.json
    current_module = read.get_current_module()
    cur.execute("SELECT id FROM modules WHERE name=?", (current_module,))
    module_id = cur.fetchone()
    cur.execute("INSERT INTO states (module_id, name) VALUES (?, ?)", (module_id[0], name))
    con.commit()
    con.close()


# Create a function that adds an event to the events table
def add_event(name, from_state, to_state, module_id):
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    cur.execute("INSERT INTO events (name, from_state, to_state, module_id) VALUES (?, ?, ?, ?)", (name, from_state, to_state, module_id))
    con.commit()
    con.close()


# Function that creates a new module in the database
def create_module(name):
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    cur.execute("INSERT INTO modules (name) VALUES (?)", (name,))
    con.commit()
    con.close()
