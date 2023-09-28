# ToDo list

## General
- [x] MVP
- [ ] Automate setup

## Utils
- [ ] Refactor functions to modules
  - [ ] update *.gz from IMDB (scraper)
  - [ ] extract *.gz to *.tsv (parser)
  - [x] import data to DB
  - [ ] get random movie for app
- [ ] setup controller.py

## DB
- [x] Setup a DB (postgresql)
  - [ ] models.py
    - [x] movies
    - [ ] watched movies
  - [ ] DB Scema
    - [x] movies
    - [ ] watched movies
  - ...

## .env
- [x] Setup an .env
- [x] .env file example

## app
- [ ] Create FstAPI app
  - [ ] Views
    - [x] homepage
    - [ ] UI for random film
  - [ ] Templates 
    - [x] Base.html
      - [x] Basic Bootstrap
      - [ ] Nav bar
      - [ ] background cover
    - [ ] Random movie
      - [x] Basic page with random movie info
      - [ ] Get random movie button
      - [ ] Parse and show movie poster
  - [ ] Controller
  - [ ] Data Adapter
  - [ ] Service
  - [ ] Logger

## Docker
- [ ] Setup Dockerfile
- [ ] Docker compose

## Tests
- [ ] Tests

## Secrets
- [ ] Secrets

## Git
- [x] init github
- [x] write a README.md