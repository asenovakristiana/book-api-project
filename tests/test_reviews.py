from fastapi.testclient import TestClient
import sys
sys.path.insert(0, ".")
from app.main import app

client = TestClient(app)

def test_add_review_for_new_book():
    review_data = {
        "book_id": 2,
        "user_name": "Bob",
        "rating": 4.7,
        "comment": "A timeless classic!"
    }
    response = client.post("/reviews/add", json=review_data)
    assert response.status_code == 200
    assert response.json()["message"] == "Review added successfully!"

def test_get_reviews():
    response = client.get("/reviews/")
    assert response.status_code == 200
    reviews = response.json()

    reviews_data = response.json()["reviews"]  
    assert any(review["book_id"] == 2 and review["comment"] == "A timeless classic!" for review in reviews_data)
