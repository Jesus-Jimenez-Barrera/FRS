"""
Access Control Model.
This Script was made by StarSoft Team.

Model designed for access control when registering an action coming from the frontend.
"""

# Import of libraries, modules and packages
import sqlite3
from datetime import datetime

def create_access_log_table():
    conn = sqlite3.connect('') # Database name
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS access_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        access_time TEXT,
        location TEXT,
        status TEXT
    )
    """)
    conn.commit()
    conn.close()

def log_access(user_id, location, status):
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO access_logs (user_id, access_time, location, status)
    VALUES (?, ?, ?, ?)
    """, (user_id, datetime.now().isoformat(), location, status))
    conn.commit()
    conn.close()