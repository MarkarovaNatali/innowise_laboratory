from pydantic import BaseModel, Field
from typing import Optional


class BookBase(BaseModel):
    """Base schema for book data."""
    title: str = Field(..., max_length=255, description="Book title")
    author: str = Field(..., max_length=100, description="Author name")
    year: Optional[int] = Field(None, ge=1500, le=2026, description="Year of publication (1500–2026)")


class BookCreate(BookBase):
    """Schema for creating a new book."""

    class Config:
        schema_extra = {
            "example": {
                "title": "The Pragmatic Programmer",
                "author": "Andrew Hunt",
                "year": 1999
            }
        }


class BookUpdate(BaseModel):
    """Schema for updating book details."""
    title: Optional[str] = Field(None, max_length=255)
    author: Optional[str] = Field(None, max_length=100)
    year: Optional[int] = Field(None, ge=1500, le=2026)


class Book(BookBase):
    """Schema for returning book data with ID."""
    id: int

    class Config:
        orm_mode = True
