from fastapi import FastAPI
from app.routers import books, reviews

app = FastAPI()

app.include_router(books.router, prefix="/books", tags=["books"])
app.include_router(reviews.router, prefix="/reviews", tags=["reviews"])

@app.get("/")
def home():
    return {"message": "Welcome to Book API!"}