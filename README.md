# imdb-random-movie

For current mvp version follow these steps:
1. setup ../.env file (Postgresql setup)
2. run ../src/utils/imdb_scraper.py
2. run ../src/utils/parser_gz_to_tsv.py
3. run ../src/handle_tsv.py
4. with "uvicorn src.app:app" 
   - go to "0.0.0.0:8000/fill_genres/"
   - go to "0.0.0.0:8000/fill_movies/"
5. use page with "uvicorn src.app:app" -> "0.0.0.0:8000/movie/"