import sqlite3
import state_bird.data.read as read


def add_state(name, bit=-1):
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    if bit == -1:
        cur.execute("SELECT id FROM modules WHERE name=?",
                    (read.get_current_module(),))
        module_id = cur.fetchone()
        max_bit = cur.execute("SELECT MAX(bit) FROM states WHERE module_id=?",
                              (module_id[0],)).fetchone()[0]
        bit_sum = cur.execute("SELECT SUM(bit) FROM states WHERE module_id=?",
                              (module_id[0],)).fetchone()[0]
        if max_bit is None:
            new_bit = 1
        elif bit_sum < (max_bit)*(max_bit+1)/2:
            new_bit = (max_bit)*(max_bit+1)/2 - bit_sum
        else:
            new_bit = max_bit + 1
        print(new_bit)
        cur.execute("INSERT INTO states (module_id, name, bit) VALUES \
                    (?, ?, ?)", (module_id[0], name, new_bit))
    # current_module = read.get_current_module()
    # cur.execute("SELECT id FROM modules WHERE name=?", (current_module,))
    # module_id = cur.fetchone()
    # cur.execute("INSERT INTO states (module_id, name, bit) VALUES \
    #             (?, ?, ?)", (module_id[0], name, -1))
    con.commit()
    con.close()


# Create a function that adds an event to the events table
def add_event(name, from_state, to_state, module_id):
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    cur.execute("INSERT INTO events (name, from_state, to_state, module_id) \
                VALUES (?, ?, ?, ?)", (name, from_state, to_state, module_id))
    con.commit()
    con.close()


# Function that creates a new module in the database
def create_module(name):
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    cur.execute("INSERT INTO modules (name) VALUES (?)", (name,))
    con.commit()
    con.close()
