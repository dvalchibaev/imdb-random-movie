import csv

YEARS = [str(y) for y in range(1940, 2024)]

class Movie:
    title: str
    year: int
    genres: list[str]
    rating: float
    votes: int

    def __init__(self, title: str, year: str, genres: str, rating='', votes=''):
        self.title, self.year, self.genres = title, int(year), genres.split(',')
        self.add_rating(rating)
        self.add_votes(votes)

    def __str__(self):
        return f"{self.title=} {self.year} {self.rating=} {self.votes=}"

    def add_rating(self, rate: str):
        if rate.replace('.','').isnumeric():
            self.rating = float(rate)
        else:
            self.rating = 0

    def add_votes(self, votes: str):
        if votes.isnumeric():
            self.votes = int(votes)
        else:
            self.votes = 0


GENRES = ["None"]
MOVIES_SNIPPET = []


with open("../../imdb/files_tsv/title.basics.tsv", "r") as f:
    columns = f.readline().split()
    movies = {}
    for line in f.readlines():
        t_id, t_type, title, _, _, year, _, _, genres = line[:-1].split('\t')
        if t_type == 'movie' and year in YEARS and genres != "\\N":
            movies[t_id] = Movie(title, year, genres)
            for genre in genres.split(','):
                if genre not in GENRES:
                    GENRES.append(genre)


with open("../data/genres.csv", "w") as f:
    rf = csv.writer(f, delimiter=";")
    rf.writerows([[genre] for genre in GENRES])


with open("../../imdb/files_tsv/title.ratings.tsv", "r") as f:
    columns = f.readline().split()
    for line in f.readlines():
        t_id, rating, votes = line[:-1].split('\t')
        if t_id in movies.keys():
            movies[t_id].add_rating(rating)
            movies[t_id].add_votes(votes)


for year in YEARS:
    with open(f"../data/movies{year}.csv", "w") as f:
        rf = csv.writer(f, delimiter=";")
        for k, v in movies.items():
            if v.rating > 0 and v.votes > 0 and v.year == int(year):
                movie = [k, v.title, v.year, v.rating, v.votes, ','.join(v.genres)]
                rf.writerow(movie)
