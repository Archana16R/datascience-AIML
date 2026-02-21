import sqlite3
import pandas as pd
import os

# If database file exists, remove it (prevents locking issues)
if os.path.exists("internship.db"):
    os.remove("internship.db")

# Create new database connection
with sqlite3.connect("internship.db") as conn:

    # Create mentors table
    conn.execute("""
    CREATE TABLE mentors (
        mentor_id INTEGER PRIMARY KEY,
        mentor_name TEXT,
        track TEXT
    );
    """)

    # Create interns table
    conn.execute("""
    CREATE TABLE interns (
        id INTEGER PRIMARY KEY,
        name TEXT,
        track TEXT,
        stipend INTEGER
    );
    """)

    # Insert mentor data
    conn.executemany("""
    INSERT INTO mentors VALUES (?, ?, ?)
    """, [
        (1, 'Rahul', 'Data Science'),
        (2, 'Sneha', 'Web Dev'),
        (3, 'Arjun', 'AI/ML')
    ])

    # Insert intern data
    conn.executemany("""
    INSERT INTO interns VALUES (?, ?, ?, ?)
    """, [
        (1, 'Asha', 'Data Science', 6000),
        (2, 'Rohan', 'Web Dev', 4500),
        (3, 'Meera', 'AI/ML', 7000),
        (4, 'Kiran', 'Data Science', 5500)
    ])

    # INNER JOIN query
    df = pd.read_sql_query("""
    SELECT i.id,
           i.name,
           i.track,
           i.stipend,
           m.mentor_name
    FROM interns i
    INNER JOIN mentors m
    ON i.track = m.track;
    """, conn)

df