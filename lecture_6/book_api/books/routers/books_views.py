from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from ..models import Book
from ..database import get_db
from ..schemas import Book as BookResponse

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/search/", response_model=List[BookResponse])
async def search_books(
        book_title: Optional[str] = Query(None, description="Filter by book title (substring match)"),
        author: Optional[str] = Query(None, description="Filter by author name (substring match)"),
        year: Optional[int] = Query(None, description="Filter by publication year"),
        db: Session = Depends(get_db),
) -> List[BookResponse]:
    """Search for books by optional filters: title, author, and year."""
    query = db.query(Book)
    if book_title:
        query = query.filter(Book.title.ilike(f"%{book_title}%"))
    if author:
        query = query.filter(Book.author.ilike(f"%{author}%"))
    if year:
        query = query.filter(Book.year == year)

    results = query.all()
    if not results:
        raise HTTPException(status_code=404, detail="No books found")
    return results
