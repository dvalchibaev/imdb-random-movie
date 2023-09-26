import uvicorn
from fastapi import Depends, FastAPI
from . import model, schemas
from .database import SessionLocal, engine
from sqlalchemy.orm import Session, aliased

import csv

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
async def root():
    return {"message": "Hello World"}


@app.get("/fill_db/")
async def fill_db(db: Session = Depends(get_db)):
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


@app.get("/fill_movies/")
async def fill_movies(db: Session = Depends(get_db)):
    with open("src/data/movies2023.csv", "r") as f:
        fr = csv.reader(f, delimiter=";")
        for line in fr:
            id, _, title, year, genres = line
            id = int(id[2:])
            movie = model.Movie(id=id, title=title, year=int(year), rating=0, votes=0)
            for genre in genres.split(','):
                print(genre)
                db_genre = db.query(model.Genre).filter(model.Genre.name==genre).first()
                print(db_genre)
                movie.genres.append(db_genre)
            db.add(movie)
    db.commit()
    return {"message": "OK"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)