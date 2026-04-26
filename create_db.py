import sqlite3

import sqlite3

con = sqlite3.connect("rms.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    course TEXT,
    roll TEXT,
    description TEXT
)
""")

con.commit()
con.close()

print("DB created successfully!")
con = sqlite3.connect("rms.db")
cur = con.cursor()

cur.execute("PRAGMA table_info(student)")
print(cur.fetchall())