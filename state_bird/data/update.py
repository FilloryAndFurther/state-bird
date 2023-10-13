import sqlite3


def delete_event(name):
    """
    Delete an event from the database.

    Args:
        name (str): The name of the event to delete.

    Returns:
        bool: True if the event was deleted, False otherwise.
    """
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    cur.execute("DELETE FROM events WHERE name=?", (name,))
    con.commit()
    con.close()
    return True


def delete_state(name):
    """
    Delete a state from the database.

    Args:
        name (str): The name of the state to delete.

    Returns:
        bool: True if the state was deleted, False otherwise.
    """
    con = sqlite3.connect('state_bird/data/database.db')
    cur = con.cursor()
    cur.execute("DELETE FROM states WHERE name=?", (name,))
    # Delete all events that have this state as a from_state or to_state
    cur.execute("DELETE FROM events WHERE from_state=?", (name,))
    cur.execute("DELETE FROM events WHERE to_state=?", (name,))
    con.commit()
    con.close()
    return True
