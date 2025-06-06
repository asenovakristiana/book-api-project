from fastapi import APIRouter
import sqlite3
from app.database import get_db_connection
def get_db_connection():
    return database.get_db_connection()

router = APIRouter()

@router.get("/books")
def get_books():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return {"books": [dict(book) for book in books]}

@router.post("/books/add")
def add_book(title: str, author: str, genre: str, rating: float, published_year: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, genre, rating, published_year) VALUES (?, ?, ?, ?, ?)",
                   (title, author, genre, rating, published_year))
    conn.commit()
    conn.close()
    return {"message": "book is added successfully"}
