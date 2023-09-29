# imdb-random-movie

## App preparation for local use
For current mvp version follow these steps:
1. create `../.env` file (Postgresql setup, excample in dummies/env_dummy)
2. run `../src/utils/imdb_scraper.py`
2. run `../src/utils/parser_gz_to_tsv.py`
3. run `../src/handle_tsv.py`
4. on root folder run in command line `$ uvicorn src.app:app`
5. To fill the local DB:
   - go to `0.0.0.0:8000/fill_genres/`
   - go to `0.0.0.0:8000/fill_movies/`

## Using the app
To use the app go to `0.0.0.0:8000/movie/`