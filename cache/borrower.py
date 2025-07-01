from data import borrowings as data
from . import redis_client

def test():
    return "redis connect ok"

def save_books(borrower):
    """borrower:{borrower}:books"""
    books = data.get_books_by_borrower(borrower)
    for book in books:
        redis_client.RPUSH(f"borrower:{borrower}:books", books)

def get_books(borrower):
    """borrower:{borrower}:books"""
    return redis_client.LRANGE("borrower:{borrower}:books", 0, -1)

def return_book(borrower):
    return redis_client.del("borrower:{borrower}:books")