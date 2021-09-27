import json
import ssl
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urlencode
import urllib
import re

#######
def get_web_page_content(url):
  req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
  webpage = urlopen(req).read()
  soup = BeautifulSoup(webpage, 'html.parser')
  return soup

def get_movie_details(dataframe, row, column):
    z = row.name # print z
    url = dataframe[column].values[row.name]
    soup = get_web_page_content(url)
    try:
        genres = soup.find("li",{"data-testid":"storyline-genres"}).get_text(strip=False)
        genres = genres.replace('Genres', '')
        genres = genres.replace('Genre', '')
        genres = re.findall('[A-Z][^A-Z]*', genres)
    except:
        genres = None
    dataframe.at[z,"genres"] = genres
    top_cast = soup.find_all("a",{"data-testid":"title-cast-item__actor"})
    stars = []
    for elem in top_cast:
        stars.append(elem.string)
    dataframe.at[z,"stars"] = stars
    try:
        media_type = soup.find("div",{"class":"TitleBlock__TitleMetaDataContainer-sc-1nlhx7j-2 hWHMKr"}).get_text(strip=False)
    except:
        media_type = None
    dataframe.at[z,"media_type"] = media_type
    try:
        num_episodes = soup.find("span",{"data-testid":"hero-subnav-bar-series-episode-count"}).get_text(strip=False)
    except:
        num_episodes = 0
    dataframe.at[z,"num_episodes"] = num_episodes
    print(url, genres, stars, media_type, "episodes: ", num_episodes)    

#######
movies = pd.read_csv("filmography_list.csv")
movies['genres'] = ''
movies['stars'] = ''
#movies['creators'] = ''
#movies['directors'] = ''
movies['media_type'] = ''
movies['num_episodes'] = ''
movies.apply(lambda row: get_movie_details(movies, row, "imdb_link"), axis=1)
movies.to_csv("snl_movies_data.csv", index=False)