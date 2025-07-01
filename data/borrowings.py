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

def get_books():
    return cur.execute("select title, author from books where available = 1")

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


