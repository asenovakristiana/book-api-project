from fastapi import APIRouter
from pydantic import BaseModel
import sqlite3
from app.database import get_db_connection

router = APIRouter()

class Book(BaseModel):
    title: str
    author: str
    genre: str
    rating: float
    published_year: int

@router.get("/")
def get_books():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return {"books": [dict(book) for book in books]}

@router.post("/add")
def add_book(book: Book):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO books (title, author, genre, rating, published_year) VALUES (?, ?, ?, ?, ?)",
        (book.title, book.author, book.genre, book.rating, book.published_year)
    )
    conn.commit()
    conn.close()
    return {"message": "Book added successfully!"}
