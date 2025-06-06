from fastapi import APIRouter
import sqlite3
from app import database

def get_db_connection():
    return database.get_db_connection()

router = APIRouter()

@router.post("/reviews/add")
def add_review(book_id: int, user_name: str, rating: float, comment: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reviews (book_id, user_name, rating, comment) VALUES (?, ?, ?, ?, ?)",
                   (book_id, user_name, rating, comment))
    conn.commit()
    conn.close()
    return {"message": " review is added successfully!"}

@router.get("/reviews/{book_id}")
def get_reviews(book_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reviews WHERE book_id = ?", (book_id,))
    reviews = cursor.fetchall()
    conn.close()
    return {"reviews": [dict(review) for review in reviews]}