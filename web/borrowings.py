from fastapi import APIRouter
from pydantic import BaseModel

from data import get_db
from service import borrowings as service

router = APIRouter(prefix="/borrows")

@router.get("")
def test():
    return service.test()

class AddBooksReq(BaseModel) :
    title: str
    author: str


@router.post("/books")
def add_book(body : AddBooksReq):
    """
    도서 제목(title), 도서 저자(author)를 받아 해당 도서를 등록한다.
    """
    return service.add_book(body.title, body.author)


@router.get("/books")
def get_books():
    """
    대출 가능한 도서 목록을 조회한다.
    """
    return service.get_books()

@router.delete("/books/{book_id}")
def delete_book(book_id: int):
    """
    도서 아이디(book_id)를 받아 대출 가능한 상태라면 해당 도서를 삭제한다.
    """
    return service.delete_book(book_id)

class BorrowReq(BaseModel) :
    borrower: str
    title: str

# ㅁㄴㅇㄹ
@router.post("/borrows")
def borrow(body : BorrowReq):
    """대출자 이름(borrower), 도서 제목(title)을 받아 해당 도서를 대출 처리한다.	"""
    return service.borrow(body.borrower, body.title

