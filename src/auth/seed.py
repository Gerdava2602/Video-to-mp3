import sqlite3

conn = sqlite3.connect("auth.db")
c = conn.cursor()
try:
    c.executescript(
        """               
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email text NOT NULL,
            password text NOT NULL
        );

        INSERT INTO users (email, password) VALUES ('german@email.com', '123');
    """
    )
    print(c.execute("SELECT * FROM users").fetchall())
    c.commit()
    c.close()
except Exception as e:
    print(e)
    pass
