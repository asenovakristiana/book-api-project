from database import get_db_connection

def get_all_books():
    """Retrieves all books from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return {"books": [dict(book) for book in books]}

def add_book(title, author, genre, rating, published_year):
    """Adds a new book to the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO books (title, author, genre, rating, published_year) VALUES (?, ?, ?, ?, ?)",
        (title, author, genre, rating, published_year)
    )
    conn.commit()
    conn.close()
    return {"message": "Book added successfully!"}

def edit_book(book_id, title, author, genre, rating, published_year):
    """Updates book information."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE books SET title=?, author=?, genre=?, rating=?, published_year=?
        WHERE id=?
    """, (title, author, genre, rating, published_year, book_id))
    conn.commit()
    conn.close()
    return {"message": "Book updated successfully!"}

def delete_book(book_id):
    """Deletes a book from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    conn.close()
    return {"message": "Book deleted successfully!"}

def search_books(query):
    """Searches for books by title or genre."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE title LIKE ? OR genre LIKE ?", (f"%{query}%", f"%{query}%"))
    books = cursor.fetchall()
    conn.close()
    return {"books": [dict(book) for book in books]}

def sort_books_by_rating():
    """Sorts books by rating in descending order."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books ORDER BY rating DESC")
    books = cursor.fetchall()
    conn.close()
    return {"books": [dict(book) for book in books]}
