from fastapi import FastAPI
from app.routers import books, reviews

app = FastAPI()

app.include_router(books.router, prefix="/api")
app.include_router(reviews.router, prefix="/api")

@app.get("/")
def home():
    return {"message": "Welcome in API for books!"}