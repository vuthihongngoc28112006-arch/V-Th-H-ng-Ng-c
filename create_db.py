import sqlite3

def create_db():
    con = sqlite3.connect("rms.db")
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS student(
        roll TEXT PRIMARY KEY,
        name TEXT,
        course TEXT
)
""")

    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS student(
        roll TEXT PRIMARY KEY,
        name TEXT,
        course TEXT
    )
    """)

    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS result(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        roll TEXT,
        name TEXT,
        course TEXT,
        marks_ob INTEGER,
        full_marks INTEGER,
        per REAL,
        credit INTEGER
    )
    """)

    con.commit()
    con.close()

create_db()

con = sqlite3.connect("rms.db")
cur = con.cursor()

# test
cur.execute("PRAGMA table_info(student)")
print(cur.fetchall())

cur.execute("PRAGMA table_info(result)")
print(cur.fetchall())

con.close()
