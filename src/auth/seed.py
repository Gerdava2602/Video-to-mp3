import sqlite3

conn = sqlite3.connect("auth.db")
c = conn.cursor()
try:
    c.execute("DROP TABLE users")
    c.executescript(
        """
        DROP TABLE users;                
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email text NOT NULL,
            password text NOT NULL
        );

        INSERT INTO users (email, password) VALUES ('german@email.com', '123');
    """
    )
except Exception as e:
    print(e)
    pass
