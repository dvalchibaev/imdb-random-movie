import csv


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


GENRES = []
MOVIES_SNIPPET = []


with open("../../imdb/files_tsv/title.basics.tsv", "r") as f:
    columns = f.readline().split()
    movies = {}
    YEARS = [str(y) for y in range(1980,2024)]
    for line in f.readlines():
        t_id, t_type, title, _, _, year, _, _, genres = line[:-1].split('\t')
        # if t_type == 'movie' and year in YEARS and "Horror" in genres:
        #     movies[t_id] = Movie(title, year, genres)
        if t_type == "movie" and genres != "\\N":
            for genre in genres.split(','):
                if genre not in GENRES:
                    GENRES.append(genre)
            if year == "2023":
                MOVIES_SNIPPET.append([t_id, t_type, title, year, genres])


with open("../genres.csv", "w") as f:
    rf = csv.writer(f, delimiter=";")
    rf.writerows([[genre] for genre in GENRES])

with open("../data/movies2023.csv", "w") as f:
    rf = csv.writer(f, delimiter=";")
    for movie in MOVIES_SNIPPET[:10]:
        rf.writerow(movie)


# with open("../../imdb/files_tsv/title.ratings.tsv", "r") as f:
#     columns = f.readline().split()
#     for line in f.readlines():
#         t_id, rating, votes = line[:-1].split('\t')
#         if t_id in movies.keys():
#             movies[t_id].add_rating(rating)
#             movies[t_id].add_votes(votes)


for k, v in movies.items():
    if v.rating > 8 and v.votes > 5000:
        print(k, v)
