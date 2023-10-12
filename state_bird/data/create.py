import sqlite3


# Create a function that adds a state to the states table
def add_state(name):
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    cur.execute("INSERT INTO states (name) VALUES (?)", (name,))
    con.commit()
    con.close()


# Create a function that adds an event to the events table
def add_event(name, from_state, to_state):
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    cur.execute("INSERT INTO events (name, from_state, to_state) VALUES (?, ?, ?)", (name, from_state, to_state))
    con.commit()
    con.close()


# Function that creates a new module in the database
def create_module(name):
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    cur.execute("INSERT INTO modules (name) VALUES (?)", (name,))
    con.commit()
    con.close()
