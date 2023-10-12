import sqlite3
import os

def init_db():
    try:
        con = sqlite3.connect('state_bird/data/database.db')
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS states 
                    (id INT PRIMARY KEY, 
                    module_id INT NOT NULL,
                    name TEXT NOT NULL)""")
        
        cur.execute("""CREATE TABLE IF NOT EXISTS modules 
                    (id INT PRIMARY KEY, 
                    name TEXT NOT NULL)""")
        

        cur.execute("""CREATE TABLE IF NOT EXISTS events (
        id INT PRIMARY KEY,
        module_id INT NOT NULL,
        name TEXT NOT NULL,
        from_state INT NOT NULL,
        to_state INT NOT NULL)""")
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