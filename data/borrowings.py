from . import con, cur

def test():
    return "sqlite connect ok"

def add_books(title, author):
    try:
        cur.execute("insert into books (title, author) values (?, ?)", (title, author))
        con.commit()
        return True
    except Exception as e:
        return False

#     cur.execute("insert into books (title, author) values (?, ?)", (title, author))
#     sqlite3.IntegrityError: UNIQUE constraint failed: books.title

class gb:
    title : str
    author : str

def get_books():
    cur.execute("select title, author from books where available = 1")
    return cur.fetchall()

def delete_books(book_id):
    try:
        cur.execute("delete from books where book_id = ?", (book_id,))
        con.commit()
        return True
    except Exception as e:
        return False

def borrow(borrower, title):
    try:
        cur.execute("select book_id from books where title = ?", (title,))
        book_id = cur.fetchone()[0]
        cur.execute("insert into borrwings(borrower) values (?)", (borrower))
        cur.execute("update borrwings set available = 0 where title = ?", (title,))
        con.commit()
    except Exception as e:
        print(e)
        return False

class asdf:
    borrow: str
    title: str
    author: str

def get_borrows_by_month(month):
    """[{borrower: 대출자, title:책제목, author:저자]"""
    cur.execute(
        "SELECT i.borrower, b.title, b.author FROM borrowings i JOIN books b ON i.book_id = b.book_id WHERE strftime('%m', i.borrowed_at) = ?",
        (month,))
    return cur.fetchall()

def return_book(title):
    try:
        # 반납했으니 이용 가능
        cur.execute("update books set available = 1 where title = ?", (title,))
        con.commit()
        return True
    except Exception as e:
        print(e)
        return False

def get_books_by_borrower(borrower):
    return cur.execute("select i.borrower,b.title FROM borrowings i JOIN books b ON i.book_id = b.book_id WHERE i.borrower = ?", (borrower,))