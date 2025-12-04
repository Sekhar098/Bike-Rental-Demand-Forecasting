import sqlite3
import os

db_path = 'instance/site.db'  # If in the same directory as the script, use this

# Ensure that you're pointing to the correct database file
if os.path.exists(db_path):
    print(f"Checking database at: {os.path.abspath(db_path)}")
else:
    print(f"Database {db_path} not found!")
    exit()

# Connect to the SQLite database
conn = sqlite3.connect(db_path)

cursor = conn.cursor()

# List all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Print the tables
print(tables)

conn.close()
