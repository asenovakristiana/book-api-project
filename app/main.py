from fastapi import FastAPI
from app.routers import books, reviews

app = FastAPI()

app.include_router(books.router, prefix="app/books")
app.include_router(reviews.router, prefix="app/reviews")

@app.get("/")
def home():
    return {"message": "Welcome to Book API!"}