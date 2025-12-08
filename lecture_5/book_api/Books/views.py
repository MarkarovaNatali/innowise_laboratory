from typing import Annotated

from fastapi import APIRouter, Path
from .schemas import New_Book

router = APIRouter(prefix="/books", tags=["Books"])


@router.post("/")
def add_a_new_book():
    return {
        "message": "Hello index!",
    }


@router.get("/")
def get_all_books():
    return {
        "books"
    }


@router.get("/search/")
def search_book():
    pass


@router.put("/{book_id}/")
def update_book_details(book_id: Annotated[int, Path(ge=1)]):
    pass


@router.delete("/{book_id}/")
def delete_a_book_by_id(book_id: int):
    pass
