import sqlite3


def init_db():
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS states (id INT PRIMARY KEY, name TEXT NOT NULL)""")

    # Create a sqlite table called events with the following columns:
    # id (integer primary key)
    # name (text not null)
    # from_state (integer not null)
    # to_state (integer not null)

    cur.execute("""CREATE TABLE IF NOT EXISTS events (
    id INT PRIMARY KEY,
    name TEXT NOT NULL,
    from_state INT NOT NULL,
    to_state INT NOT NULL)""")
    con.commit()
    con.close()
