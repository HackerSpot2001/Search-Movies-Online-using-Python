# pip install IMDbPY
from imdb import IMDb

im = IMDb()
search = im.search_movie("3 idiots")
for show in search:
    print(show)