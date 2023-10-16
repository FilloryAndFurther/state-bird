import sqlite3
import os


def init_db():
    """
    Initializes the database for the State Bird application by creating the
    necessary tables if they do not already exist.

    Returns:
        None
    """
    try:
        con = sqlite3.connect('state_bird/data/database.db')
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS states
                    (id INTEGER PRIMARY KEY,
                    module_id INT NOT NULL,
                    name TEXT NOT NULL,
                    bit INT NOT NULL)""")
        
        cur.execute("""CREATE TABLE IF NOT EXISTS modules
                    (id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL)""")
        
        cur.execute("""CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY,
        module_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        from_state INTEGER NOT NULL,
        to_state INTEGER NOT NULL,
        bit INT NOT NULL)""")
        
        cur.execute("""CREATE TABLE IF NOT EXISTS inputs (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        slot INTEGER NOT NULL)""")
        
        cur.execute("""CREATE TABLE IF NOT EXISTS outputs (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        slot INTEGER NOT NULL)""")
        
        con.commit()
        con.close()
    except sqlite3.Error as e:
        print(e)


def clear_db():
    file_path = 'state_bird/data/database.db'
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print("The file does not exist")