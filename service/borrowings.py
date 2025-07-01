from data import borrowings as data
from cache import borrower as cache

def test():
    db_test = data.test()
    redis_test = cache.test()
    return {"sqlite": db_test, "redis": redis_test}

def add_book(title, author):
    """
    도서 제목(title), 도서 저자(author)를 받아 해당 도서를 등록한다.
    """
    return data.add_books(title,author)

def get_books():
    return data.get_books()


def delete_book(book_id):
    return data.delete_books(book_id)

def borrow(borrower, title):
    return data.borrow(borrower, title)

def get_borrows_by_month(month):
    return data.get_borrows_by_month(month)

def return_book(title):
    return data.return_book(title)

def save_books(borrower):
    return cache.save_books(borrower)