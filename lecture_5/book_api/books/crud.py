from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Annotated

from .models import Book
from .database import get_db
from .schemas import Book as BookResponse, BookCreate, BookUpdate

router = APIRouter(prefix="/books", tags=["books"])


@router.post("/", response_model=BookResponse)
async def add_a_new_book(book: BookCreate, db: Session = Depends(get_db)) -> BookResponse:
    """Add a new book to the collection."""
    db_book = Book(title=book.title, author=book.author, year=book.year)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@router.get("/", response_model=List[BookResponse])
async def get_all_books(db: Session = Depends(get_db)) -> List[BookResponse]:
    """Retrieve all books from the collection."""
    return db.query(Book).all()


@router.put("/{book_id}", response_model=BookResponse)
async def update_book_details(
        book_id: Annotated[int, Path(..., ge=1)],
        book_update: BookUpdate,
        db: Session = Depends(get_db),
) -> BookResponse:
    """Update details of a book by its ID."""
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    if book_update.title is not None:
        book.title = book_update.title
    if book_update.author is not None:
        book.author = book_update.author
    if book_update.year is not None:
        book.year = book_update.year

    db.commit()
    db.refresh(book)
    return book


@router.delete("/{book_id}", response_model=BookResponse)
async def delete_a_book_by_id(book_id: Annotated[int, Path(..., ge=1)], db: Session = Depends(get_db)) -> BookResponse:
    """Delete a book by its ID."""
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()
    return book

