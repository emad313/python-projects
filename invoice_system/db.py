import sqlite3
import os

def init_db():
    os.makedirs('data', exist_ok=True)  # Ensure the data folder exists

    conn = sqlite3.connect('data/invoices.db')
    c = conn.cursor()

    # Clients table
    c.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, 
            email TEXT NOT NULL UNIQUE, 
            address TEXT
        )
    ''')

    # Invoices table
    c.execute('''
        CREATE TABLE IF NOT EXISTS invoices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER NOT NULL,
            date TEXT,
            due_date TEXT,
            total REAL,
            paid INTEGER DEFAULT 0,
            FOREIGN KEY (client_id) REFERENCES clients(id)
        )
    ''')

    # Invoice Items table
    c.execute('''
        CREATE TABLE IF NOT EXISTS invoice_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            invoice_id INTEGER NOT NULL,
            description TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            FOREIGN KEY (invoice_id) REFERENCES invoices(id)
        )
    ''')

    conn.commit()
    conn.close()
