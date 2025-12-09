from fastapi import FastAPI, HTTPException
from typing import Optional, List, Dict
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int


class BookCreate(BaseModel):
    title: str
    author: str
    year: int


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
    new_book_id = max(b["id"] for b in books) + 1
    new_book = {"id": new_book_id, "title": book.title, "author": book.author, "year": book.year}
    books.append(new_book)
    return Book(**new_book)


@app.get("/books/")
async def get_all_books() -> List[Book]:
    return [Book(**book) for book in books]


@app.delete("/books/{book_id}")
async def delete_a_book_by_id(book_id: int) -> Book:
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return Book(**book)
    raise HTTPException(status_code=404, detail="Book not found")


@app.put("/books/{book_id}")
async def update_book_details(book_id: int, book_update: BookUpdate) -> Book:
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
        book_title: Optional[str] = None,
        author: Optional[str] = None,
        year: Optional[int] = None
) -> Dict[str, Optional[Book]]:
    # фильтруем список по всем переданным параметрам
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
        return {"results": None}


@app.get("/books/{book_id}/")
async def get_book(book_id: int) -> Book:
    for book in books:
        if book["id"] == book_id:
            return Book(**book)
    raise HTTPException(status_code=404, detail='Book not found')
