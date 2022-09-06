# pip install tmdbv3api
from tmdbv3api import TMDb

apiKey = "9df43a67dde8f4495d8d62d23563ccaa"
url = "https://api.themoviedb.org/3/movie/550?api_key=9df43a67dde8f4495d8d62d23563ccaa"
imageUrl = "https://image.tmdb.org/t/p/w500/poster_path"

t = TMDb()
t.api_key = apiKey
t.debug = True
t.language = "en"
from tmdbv3api import Movie
movie = Movie()
search = movie.search('avengers')
with open("file.json","w") as f:
    f.write(str(search))
    #for res in search:
        #print(res.id)
        #print(res.title)
        #print(res.overview)
        #print(res.poster_path)
        #print(res.vote_average)
        #print("-"*100)


"""
recommendations = movie.recommendations(movie_id=111)
for recommendation in recommendations:
    print(recommendation)

from tmdbv3api import Movie
movie = Movie()
recommendations = movie.recommendations(movie_id=111)
for recommendation in recommendations:
    print(recommendation.title)
    print(recommendation.overview)

populars = movie.popular()
for popular in populars:
    print(popular.id)
    print(popular.title)
    print(popular.overview)
    print(popular.poster_path)
    print(popular.poster_path)
    print("-"*100)

m = movie.details(343611)
print(m.title)
print(m.overview)
print(m.popularity)

search = movie.search('avengers')
for res in search:
    print(res.id)
    print(res.title)
    print(res.overview)
    print(res.poster_path)
    print(res.vote_average)
    print("-"*100)

similar = movie.similar(777)
for result in similar:
    print(result.id)
    print(result.title)
    print(result.overview)
    print("-"*100)
"""
"""
from tmdbv3api import TV
tv = TV()
shows = tv.search("matsya kaand")
for show in shows:
    print(show.id)
    print(show.name)
    print(show.poster_path)
    print(show.vote_average)
    print(show.overview)
    print("*"*100)

similars = tv.similar(62560)
for show in similars:
    print(show)
    print("*"*100)

"""
"""
from tmdbv3api import Season
season = Season()
show_season = season.details(1396, 1)
print(show_season.air_date)
print(len(show_season.episodes))
"""
"""
from tmdbv3api import Person
person = Person()
p = person.details(12)
print(p.name)
print(p.biography)
"""
"""
from tmdbv3api import Discover
discover = Discover()
movies = discover.discover_movies({
    'primary_release_date.gte': '2017-01-20',
    'primary_release_date.lte': '2017-01-25'
})
movies = discover.discover_movies({
    'sort_by': 'popularity.desc'
})

movies = discover.discover_movies({
    'certification_country': 'US',
    'certification.lte': 'G',
    'sort_by': 'popularity.desc'
})
for movie in movies:
    print(movie)
    print("*"*100)

show = discover.discover_tv_shows({
    'sort_by': 'popularity.desc'
})

show = discover.discover_tv_shows({
    'with_genres': 18,
    'sort_by': 'vote_average.desc',
    'vote_count.gte': 10
})

"""
"""
from tmdbv3api import Account
from tmdbv3api import Authentication
from tmdbv3api import TMDb, Movie

USERNAME = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD"

tmdb = TMDb()
tmdb.api_key = "YOUR_API_KEY"

auth = Authentication(username=USERNAME, password=PASSWORD)

account = Account()
details = account.details()

print("You are logged in as %s. Your account ID is %s." % (details.username, details.id))
print("This session expires at: %s" % auth.expires_at)

movie = Movie()

s = movie.search("Gangs of New York")
first_result = s[0]
recommendations = movie.recommendations(first_result.id)

for recommendation in recommendations:
    print("Adding %s (%s) to watchlist." % (recommendation.title, recommendation.release_date))
    account.add_to_watchlist(details.id, recommendation.id, "movie")
"""
