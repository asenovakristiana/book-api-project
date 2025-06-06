from database import get_db_connection

def get_all_books():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return books

def add_book(title, author, genre, rating, published_year):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, genre, rating, published_year) VALUES (?, ?, ?, ?, ?)",
                   (title, author, genre, rating, published_year))
    conn.commit()
    conn.close()