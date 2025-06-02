from fastapi import FastAPI, HTTPException
from typing import List
from uuid import uuid4, UUID
from pydantic import BaseModel


class BookCreate(BaseModel):
    title: str
    author: str
    description: str

class Book(BookCreate):
    id: UUID

app = FastAPI()

books: List[Book] = []

@app.post("/books", response_model=Book)
def add_book(book_data: BookCreate):
    for book in books:
        if book.title == book_data.title and book.author == book_data.author:
            raise HTTPException(status_code=400, detail="Book already exists")
    book = Book(id=uuid4(), **book_data.dict())
    books.append(book)
    return book

@app.get("/books", response_model=List[Book])
def list_books():
    return books

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: UUID):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: UUID):
    for i, book in enumerate(books):
        if book.id == book_id:
            del books[i]
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")


