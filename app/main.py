from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI
from app.routers import books, reviews

app = FastAPI()

app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(reviews.router, prefix="/reviews", tags=["Reviews"])

@app.get("/")
def home():
    return {"message": "Welcome to Book API!"}

@app.get("/openapi.json", include_in_schema=False)
def custom_openapi():
    return get_openapi(title="Book API", version="1.0", routes=app.routes)