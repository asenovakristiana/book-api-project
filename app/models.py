import sqlite3
conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    genre TEXT,
    rating REAL,
    published_year INTEGER
)    
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    user_name TEXT NOT NULL,
    rating REAL NOT NULL,
    comment TEXT,
    FOREIGN KEY(book_id) REFERENCES books(id) ON DELETE CASCADE
)
""")