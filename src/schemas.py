from typing import Optional, List

from pydantic import BaseModel


class GenreSchema(BaseModel):
    id: Optional[int]
    name: str

    class Config:
        orm_mode = True


class MovieSchema(BaseModel):
    id: Optional[str]
    title: str
    year: int
    rating: float
    votes: int