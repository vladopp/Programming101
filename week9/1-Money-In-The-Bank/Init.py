import sqlite3


conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT,
                login_attempts INTEGER DEFAULT 0,
                last_attempt REAL DEFAULT 0)'''

    cursor.execute(create_query)

create_clients_table()
