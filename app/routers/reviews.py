from fastapi import APIRouter
from pydantic import BaseModel
import sqlite3
from app.database import get_db_connection

router = APIRouter()

class Review(BaseModel):
    book_id: int
    user_name: str
    rating: float
    comment: str

@router.post("/add")
def add_review(review: Review):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO reviews (book_id, user_name, rating, comment) VALUES (?, ?, ?, ?)",
        (review.book_id, review.user_name, review.rating, review.comment)
    )
    conn.commit()
    conn.close()
    return {"message": "Review added successfully!"}

@router.get("/{book_id}")
def get_reviews(book_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reviews WHERE book_id = ?", (book_id,))
    reviews = cursor.fetchall()
    conn.close()
    return {"reviews": [dict(review) for review in reviews]}

@router.get("/")
def get_all_reviews():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reviews")
    reviews = cursor.fetchall()
    conn.close()
    return {"reviews": [dict(review) for review in reviews]}
