import sqlite3
from app.database import get_db_connection

DATABASE_NAME = "books.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def initialize_database():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT NOT NULL,
                   author TEXT NOT NULL,
                   genre TEXT NOT NULL,
                   rating REAL NOT NULL,
                   published_year INTEGER NOT NULL
    )
    """)

    books_data = [
        ("1984", "George Orwell", "Dystopian", 4.9, 1949),
        ("To Kill a Mockingbird", "Harper Lee", "Classic", 4.8, 1960),
        ("The Great Gatsby", "F. Scott Fitzgerald", "Novel", 4.7, 1925)
    ]

    cursor.executemany("INSERT INTO books (title, author, genre, rating, published_year) VALUES (?, ?, ?, ?, ?)", books_data)
    
    conn.commit()
    conn.close()
    print("Database initialized with books!")

initialize_database()
