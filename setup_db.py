import sqlite3

conn = sqlite3.connect('campus.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
''')
c.execute("INSERT OR IGNORE INTO users (username,password) VALUES (?,?)", ("testuser","12345"))
conn.commit()
conn.close()

print("Database created and test user added!")