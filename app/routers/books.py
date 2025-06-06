from fastapi import APIRouter, HTTPException
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
    
    if not books:
        raise HTTPException(status_code=404, detail="No books found")
    
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

@router.put("/edit/{book_id}")
def edit_book(book_id: int, book: Book):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE id=?", (book_id,))
    existing_book = cursor.fetchone()

    if not existing_book:
        raise HTTPException(status_code=404, detail="Book not found")

    cursor.execute("""
        UPDATE books SET title=?, author=?, genre=?, rating=?, published_year=?
        WHERE id=?
    """, (book.title, book.author, book.genre, book.rating, book.published_year, book_id))
    conn.commit()
    conn.close()
    return {"message": "Book updated successfully!"}

@router.delete("/delete/{book_id}")
def delete_book(book_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE id=?", (book_id,))
    existing_book = cursor.fetchone()

    if not existing_book:
        raise HTTPException(status_code=404, detail="Book not found")

    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    conn.close()
    return {"message": "Book deleted successfully!"}

@router.get("/search/")
def search_books(query: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE title LIKE ? OR genre LIKE ?", (f"%{query}%", f"%{query}%"))
    books = cursor.fetchall()
    conn.close()
    
    if not books:
        raise HTTPException(status_code=404, detail="No books found matching the query")
    
    return {"books": [dict(book) for book in books]}

@router.get("/sort/")
def sort_books_by_rating():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books ORDER BY rating DESC")
    books = cursor.fetchall()
    conn.close()
    
    if not books:
        raise HTTPException(status_code=404, detail="No books found to sort")
    
    return {"books": [dict(book) for book in books]}
