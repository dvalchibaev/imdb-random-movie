import uvicorn
from fastapi import Depends, FastAPI
from . import model, schemas
from .database import SessionLocal, engine
from sqlalchemy.orm import Session, aliased

import csv
from random import choice

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

movie_alias = aliased(model.Movie, name="m")
genre_alias = aliased(model.Genre, name="g")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root(db: Session = Depends(get_db)):
    genre = db.query(model.Genre).filter(model.Genre.name == "Horror").first()
    random_movies = db.query(model.Movie).filter(model.Movie.rating > 6.5,
                                                 model.Movie.votes > 2500,
                                                 model.Movie.genres.contains(genre)).all()
    movie = choice(random_movies)
    return {
        "id": f"tt{movie.id:07d}",
        "title": f"{movie.title}",
        "year": f"{movie.year}",
        "rating": f"{movie.rating}",
        "votes": f"{movie.votes}"
    }


@app.get("/fill_genres/")
async def fill_genres(db: Session = Depends(get_db)):
    with open("src/genres.csv", "r") as f:
        for line in f.readlines():
            db_genre = model.Genre(name=line[:-1])
            db.add(db_genre)
            db.commit()
    return {"message": "OK"}


@app.get("/get_genres/")
async def get_genres(db: Session = Depends(get_db)):
    query = db.query(model.Genre).filter(model.Genre.name == "News\n").first()
    return query


def read_movies_csv(year: str):
    result = []
    with open(f"src/data/movies{year}.csv", "r") as f:
        fr = csv.reader(f, delimiter=";")
        for line in fr:
            id, title, mv_year, rating, votes, genres = line
            id = int(id[2:])
            genres = genres.split(",")
            result.append([id, title, mv_year, rating, votes, genres])
        return result


@app.get("/fill_movies/")
async def fill_movies(db: Session = Depends(get_db)):
    for mv_year in range(1940, 2023):
        lines = read_movies_csv(str(mv_year))
        for line in lines:
            id, title, year, rating, votes, genres = line
            if not db.query(model.Movie).filter(model.Movie.id == id).first():
                movie = model.Movie(id=id, title=title, year=int(year),
                                    rating=float(rating), votes=int(votes))
                for genre in genres:
                    db_genre = db.query(model.Genre).filter(model.Genre.name == genre).first()
                    movie.genres.append(db_genre)
                db.add(movie)
        db.commit()
    return {"message": f"OK"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)