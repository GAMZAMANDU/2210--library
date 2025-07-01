from fastapi import APIRouter
from pydantic import BaseModel

from cache import borrower
from data import get_db
from service import borrowings as service

router = APIRouter(prefix="/borrows")

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
@router.post("")
def borrow(body : BorrowReq):
    """대출자 이름(borrower), 도서 제목(title)을 받아 해당 도서를 대출 처리한다.	"""
    return service.borrow(body.borrower, body.title)


@router.get("/month/{borrow_month}")
def get_borrows_by_month(borrow_month: str):
    """대출이 있었던 월(borrow_month)을 받아 해당 월에 대출이 있었던 책들의 목록을 조회한다."""
    return service.get_borrows_by_month(borrow_month)

class BookReturnReq(BaseModel) :
    title: str

@router.post("/return")
def return_book(body : BookReturnReq):
    """대출자 이름(borrower), 도서 제목(title)을 받아 해당 도서를 반납 처리한다."""
    return service.return_book(body.title)

# Redis
# Http가 안적혀있음..

@router.get("/save/")
def save_book(borrower):
    """대출자의 대출한 도서 제목을 저장한다.	"""
    return service.save_books(borrower)

@router.get("/get_books")
def get_books():
    return service.get_books(borrower)