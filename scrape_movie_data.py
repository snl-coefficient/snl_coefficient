import json
import ssl
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urlencode
import urllib
import re
import time
import csv
import os

#######
def get_web_page_content(url):
  req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
  ssl._create_default_https_context = ssl._create_unverified_context
  webpage = urlopen(req).read()
  soup = BeautifulSoup(webpage, 'html.parser')
  return soup

def get_movie_details(dataframe, row, column):
    z = row.name # print z
    url = dataframe[column].values[row.name]
    print(url)
    try:
        soup = get_web_page_content(url)
    except:
        print("gotta sleep for a bit")
        time.sleep(1000)
        print("sleep over")
        soup = get_web_page_content(url)
    try:
        genres_captured = soup.find_all("a",class_="GenresAndPlot__GenreChip-cum89p-3 fzmeux ipc-chip ipc-chip--on-baseAlt")
        genres = []
        for genre in genres_captured:
            genre = genre.get_text(strip=False)
            genres.append(genre)
    except:
        genres = None
    dataframe.at[z,"genres"] = genres
    top_cast = soup.find_all("a",{"data-testid":"title-cast-item__actor"})
    stars = []
    for elem in top_cast:
        stars.append(elem.string)
    dataframe.at[z,"stars"] = stars
    try:
        media_type_captured = soup.find("div",{"class":"TitleBlock__TitleMetaDataContainer-sc-1nlhx7j-2 hWHMKr"})#.get_text(strip=False)
        media_type_reviewed = media_type_captured.find_all('li')
        media_type = []
        for media in media_type_reviewed:
            media = media.get_text(strip=False)
            media_type.append(media)
    except:
        media_type = None
    dataframe.at[z,"media_type"] = media_type
    try:
        num_episodes = soup.find("div",{"data-testid":"episodes-header"}).get_text(strip=False)
        num_episodes = num_episodes.split("Episodes")[1]
    except:
        num_episodes = 0
    dataframe.at[z,"num_episodes"] = num_episodes
    try:
        principal_people = []
        creators = soup.find_all("ul",{"class":"ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content baseAlt"})
        for creator in creators:
            people = creator.find_all("a")
            for person in people:
                indiv = person.get_text(strip=False)
                principal_people.append(indiv)
    except:
        principal_people = None
    dataframe.at[z,"principal_people"] = creators
    try:
        production_companies_captured = soup.find("li", {"data-testid":"title-details-companies"})
        production_companies_reviewed = production_companies_captured.find_all('a')
        production_companies = []
        for production in production_companies_reviewed:
            production = production.get_text(strip=False)
            production_companies.append(production)
            production_companies.remove('Production companies')
    except:
        production_companies = None
    dataframe.at[z,"production_companies"]
    time.sleep(5)

#######
movies = pd.read_csv("snl_movies_credits.csv")
movies['genres'] = ''
movies['stars'] = ''
movies['media_type'] = ''
movies['num_episodes'] = ''
movies['principal_people'] = '' #should see if i can stop it from doing the same as cast
movies['production_companies'] = ''
#if os.path.exists("raw_snl_movies_data.csv"):
#    print("some of these links have already been scraped")
#    already_finished = pd.read_csv("raw_snl_movies_data.csv")
#    already_finished_urls = already_finished['imdb_link'].to_list()
#    print(already_finished_urls)
#    movies = ~movies.imdb_link.isin(already_finished_urls).copy()
#    print(movies.shape[0])
movies.apply(lambda row: get_movie_details(movies, row, "imdb_link"), axis=1)
#try: 
#    movies = pd.concat([movies, already_finished], ignore_index=True)
#except:
#    print("could not append")
movies.to_csv("raw_snl_movies_data.csv", index=False)
