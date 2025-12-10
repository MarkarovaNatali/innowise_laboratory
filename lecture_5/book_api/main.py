from fastapi import FastAPI, HTTPException, Path, Query
from typing import Optional, List, Dict, Annotated
from pydantic import BaseModel, Field

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int = Field(..., ge=1500, le=2026)


class BookCreate(BaseModel):
    title: str
    author: str
    year: int = Field(..., ge=1500, le=2026)


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None


books = [
    {"id": 1, "title": "title_1", "author": "author_1", "year": 1990},
    {"id": 2, "title": "title_2", "author": "author_2", "year": 1990},
    {"id": 3, "title": "title_3", "author": "author_3", "year": 1990},
]


@app.post("/books/")
async def add_a_new_book(book: BookCreate) -> Book:
    """
    Add a new book to the collection.

    Args:
        book (BookCreate): Data for creating a new book.

    Returns:
        Book: The newly added book.
    """
    new_book_id = max((b["id"] for b in books), default=0) + 1
    new_book = {"id": new_book_id, "title": book.title, "author": book.author, "year": book.year}
    books.append(new_book)
    return Book(**new_book)


@app.get("/books/")
async def get_all_books() -> List[Book]:
    """
    Retrieve all books from the collection.

    Returns:
        List[Book]: A list of all books.
    """
    return [Book(**book) for book in books]


@app.delete("/books/{book_id}")
async def delete_a_book_by_id(book_id: Annotated[int, Path(..., title='The ID of the book we are deleting',
                                                           ge=1)]) -> Book:
    """
    Delete a book by its ID.

    Args:
        book_id (int): The ID of the book to delete.

    Returns:
        Book: The deleted book.

    Raises:
        HTTPException: If the book is not found.
    """
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return Book(**book)
    raise HTTPException(status_code=404, detail="Book not found")


@app.put("/books/{book_id}")
async def update_book_details(book_id: Annotated[int, Path(..., title='The ID of the book we are updating', ge=1)],
                              book_update: BookUpdate) -> Book:
    """
    Update details of a book by its ID.

    Args:
        book_id (int): The ID of the book to update.
        book_update (BookUpdate): Fields to update.

    Returns:
        Book: The updated book.

    Raises:
        HTTPException: If the book is not found.
    """
    for book in books:
        if book["id"] == book_id:
            if book_update.title is not None:
                book["title"] = book_update.title
            if book_update.author is not None:
                book["author"] = book_update.author
            if book_update.year is not None:
                book["year"] = book_update.year
            return Book(**book)
    raise HTTPException(status_code=404, detail="Book not found")


@app.get("/books/search/")
async def search_books(
        book_title: Optional[str] = Query(None),
        author: Optional[str] = Query(None),
        year: Optional[int] = Query(None),
) -> Dict[str, List[Book]]:
    """
    Search for books by title, author, or year.

    Args:
        book_title (Optional[str]): Filter by book title.
        author (Optional[str]): Filter by author name.
        year (Optional[int]): Filter by publication year.

    Returns:
        Dict[str, List[Book]]: A dictionary with search results.
    """
    results = []
    for book in books:
        if book_title and book["title"] != book_title:
            continue
        if author and book["author"] != author:
            continue
        if year and book["year"] != year:
            continue
        results.append(Book(**book))
    if results:
        return {"results": results}
    else:
        return {"results": []}


@app.get("/books/{book_id}/")
async def get_book(book_id: Annotated[int, Path(..., title='The ID of the book we are looking for', ge=1)]) -> Book:
    """
    Retrieve a single book by its ID.

    Args:
        book_id (int): The ID of the book to retrieve.

    Returns:
        Book: The requested book.

    Raises:
        HTTPException: If the book is not found.
    """
    for book in books:
        if book["id"] == book_id:
            return Book(**book)
    raise HTTPException(status_code=404, detail='Book not found')
