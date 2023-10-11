# File that contains the functions to read the data from the database
# Path: app/data/read.py

import sqlite3


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
