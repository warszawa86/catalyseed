import sqlite3
from flask import g

DATABASE = '../metadata.db'

def get_db():
    """Connect to the database and return the connection."""
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = sqlite3.connect(DATABASE)
    return g.sqlite_db

def query_db(query, args=(), one=False):
    """Execute a query and return the result."""
    cur = get_db().cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    return (rv[0] if rv else None) if one else rv

def close_db(e=None):
    """Close the database connection."""
    db = getattr(g, 'sqlite_db', None)
    if db is not None:
        db.close()
