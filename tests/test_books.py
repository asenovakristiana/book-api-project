from fastapi.testclient import TestClient
import sys
sys.path.insert(0, ".")
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Book API!"}

def test_add_new_book():
    new_book = {
        "title": "Brave new world",
        "author": "Aldous Huxley",
        "genre": "Dystopian",
        "rating": 4.8,
        "published_year": 1932
    }
    response = client.post("/books/add", json=new_book)
    assert response.status_code == 200
    assert response.json() == {"message": "Book added successfully!"}

def test_get_books():
    response = client.get("/books/")
    assert response.status_code == 200
    books = response.join()

    assert any(book["title"] == "Brave new world" for book in books)

    