import sqlite3
import state_bird.data.read as read


def add_state(name, bit=-1):
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    cur.execute("SELECT id FROM modules WHERE name=?",
                (read.get_current_module(),))
    module_id = cur.fetchone()
    if bit == -1:
        max_bit = cur.execute("SELECT MAX(bit) FROM states WHERE module_id=?",
                              (module_id[0],)).fetchone()[0]
        bit_sum = cur.execute("SELECT SUM(bit) FROM states WHERE module_id=?",
                              (module_id[0],)).fetchone()[0]
        # If the highest bit is 6, then the sum of the bits should be 21
        # But if the sum is 17, then 4 is missing, so fill that in first.
        if max_bit is None:
            new_bit = 1
        elif bit_sum < (max_bit)*(max_bit+1)/2:
            new_bit = (max_bit)*(max_bit+1)/2 - bit_sum
        else:
            new_bit = max_bit + 1
    else:
        new_bit = bit
    cur.execute("INSERT INTO states (module_id, name, bit) VALUES \
                (?, ?, ?)", (module_id[0], name, new_bit))
    con.commit()
    con.close()


# Create a function that adds an event to the events table
def add_event(name, from_state, to_state, module_id, bit=-1):
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    if bit == -1:
        cur.execute("SELECT id FROM modules WHERE name=?",
                    (read.get_current_module(),))
        module_id = cur.fetchone()
        max_bit = cur.execute("SELECT MAX(bit) FROM events WHERE module_id=?",
                              (module_id[0],)).fetchone()[0]
        bit_sum = cur.execute("SELECT SUM(bit) FROM events WHERE module_id=?",
                              (module_id[0],)).fetchone()[0]
        if max_bit is None:
            new_bit = 1
        elif bit_sum < (max_bit)*(max_bit+1)/2:
            new_bit = (max_bit)*(max_bit+1)/2 - bit_sum
        else:
            new_bit = max_bit + 1
        print(new_bit)
        cur.execute("INSERT INTO events (name, from_state, to_state, module_id\
            ,bit) VALUES (?, ?, ?, ?, ?)", (name, from_state, to_state,
                                            module_id[0], new_bit))
    con.commit()
    con.close()


# Function that creates a new module in the database
def create_module(name):
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    cur.execute("INSERT INTO modules (name) VALUES (?)", (name,))
    con.commit()
    con.close()


def create_input(name, slot):
    name = f'{name}'
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    cur.execute("INSERT INTO inputs (name, slot) VALUES (?, ?)", (name, slot))
    con.commit()
    con.close()


def create_output(name, slot):
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    cur.execute("INSERT INTO outputs (name, slot) VALUES (?, ?)", (name, slot))
    con.commit()
    con.close()


def delete_input(name):
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    cur.execute("DELETE FROM inputs WHERE name=?", (name,))
    con.commit()
    con.close()


def delete_output(name):
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    cur.execute("DELETE FROM outputs WHERE name=?", (name,))
    con.commit()
    con.close()
