from fastapi.testclient import TestClient
import sys
sys.path.insert(0, ".")
from app.main import app

client = TestClient(app)

# Test home endpoint
def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Book API!"}

# Test adding a new book
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

# Test retrieving all books
def test_get_books():
    response = client.get("/books/")
    assert response.status_code == 200
    
    books_data = response.json()["books"] 
    assert any(book["title"] == "Brave new world" for book in books_data)

# Test editing a book
def test_edit_book():
    updated_book = {
        "title": "Brave New World - Updated",
        "author": "Aldous Huxley",
        "genre": "Sci-Fi",
        "rating": 4.9,
        "published_year": 1932
    }
    response = client.put("/books/edit/1", json=updated_book)
    assert response.status_code == 200
    assert response.json() == {"message": "Book updated successfully!"}

# Test deleting a book
def test_delete_book():
    response = client.delete("/books/delete/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Book deleted successfully!"}

# Test searching for a book
def test_search_books():
    response = client.get("/books/search?query=Brave")
    assert response.status_code == 200

    books_data = response.json()["books"]
    assert any("Brave" in book["title"] for book in books_data)

# Test sorting books by rating
def test_sort_books_by_rating():
    response = client.get("/books/sort")
    assert response.status_code == 200

    books_data = response.json()["books"]
    ratings = [book["rating"] for book in books_data]
    assert ratings == sorted(ratings, reverse=True)

# Test adding a review
def test_add_review():
    review_data = {
        "book_id": 1,
        "user_name": "Alice",
        "rating": 4.5,
        "comment": "Amazing book!"
    }
    response = client.post("/reviews/add", json=review_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Review added successfully!"}

# Test retrieving reviews for a book
def test_get_reviews():
    response = client.get("/reviews/1")
    assert response.status_code == 200

    reviews_data = response.json()["reviews"]
    assert any(review["comment"] == "Amazing book!" for review in reviews_data)
