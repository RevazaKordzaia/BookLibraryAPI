from typing import Optional
from pydantic import BaseModel
from uuid import UUID

class BookCreate(BaseModel):
    title: str
    author: str
    year: int
    genre: Optional[str] = None

class Book(BookCreate):
    id: UUID
