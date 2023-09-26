from sqlalchemy import Column, ForeignKey, Integer, String, Float, Table, DECIMAL
from sqlalchemy.orm import relationship
from .database import Base


movie_genre = Table(
    "movie_genre",
    Base.metadata,
    Column("genre_id", ForeignKey("genres.id"), primary_key=True),
    Column("movie_id", ForeignKey("movies.id"), primary_key=True)
)


class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))

    movies = relationship("Movie", secondary="movie_genre", back_populates="genres")
    # def __str__(self):
    #     return f"{self.name}"
    #
    # def __repr__(self):
    #     return f"<genre: {self.name}>"


class Movie(Base):
    __tablename__ = "movies"
    id = Column(String, primary_key=True)
    title = Column(String(500))
    year = Column(Integer)
    rating = Column(Float)
    votes = Column(Integer)

    genres = relationship("Genre", secondary="movie_genre", back_populates="movies")

    # def __repr__(self):
    #     return (f"<title: {self.title}> <year: {self.year}> "
    #             f"<rating: {self.rating}> <votes: {self.votes}>")
    #
    # def __str__(self):
    #     return f"{self.title} ({self.year}), {self.rating:.1f} ({self.votes} votes)"
