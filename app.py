import sqlite3
import tkinter as tk
from tkinter import ttk

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('database.db')
cur = conn.cursor()

# Create table if not exists
cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

# Insert sample data if table is empty
cur.execute('SELECT COUNT(*) FROM users')
count = cur.fetchone()[0]
if count == 0:
    sample_users = [
        ('Alice', 'alice@example.com'),
        ('Bob', 'bob@example.com'),
        ('Charlie', 'charlie@example.com'),
    ]
    cur.executemany('INSERT INTO users (name, email) VALUES (?, ?)', sample_users)
    conn.commit()

# Fetch all users
cur.execute('SELECT id, name, email FROM users')
rows = cur.fetchall()

# Setup Tkinter window
root = tk.Tk()
root.title('SQLite Data Display')

# Create Treeview widget to display data in table format
columns = ('id', 'name', 'email')
tree = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col.title())
    tree.column(col, anchor='center')

tree.pack(expand=True, fill='both')

# Insert rows into Treeview
for row in rows:
    tree.insert('', tk.END, values=row)

# Start Tkinter main loop
root.mainloop()

