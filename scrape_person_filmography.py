import json
import ssl
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urlencode
import urllib

#######
def get_web_page_content(url):
  req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
  webpage = urlopen(req).read()
  soup = BeautifulSoup(webpage, 'html.parser')
  return soup

def get_movie_info(bs4_result, person, id, dataframe):
    odd_rows = bs4_result.find_all('div', class_=id)
    for movie in odd_rows:
        credit_type = movie.get('id')
        year = movie.find('span','year_column').contents[0]
        year = year.strip()
        title = movie.find('a').contents[0]
        title = title.strip()
        link = movie.find('a')['href']
        imdb_link = 'https://www.imdb.com' + link
        add_info = movie.get_text()
        add_info = add_info.strip()
        episode_count = len(movie.findAll('div', {'class': 'filmo-episodes'}))
        dataframe.loc[len(dataframe.index)] = [person, credit_type, year, title, imdb_link, episode_count, add_info]

def get_person_filmography(dataframe, row, column):
    z = row.name
    person = dataframe["person"].values[z]
    print(person)
    imdb_link = dataframe[column].values[z]
    soup = get_web_page_content(imdb_link)
    get_movie_info(soup, person, 'filmo-row odd', filmography)
    get_movie_info(soup, person, 'filmo-row even', filmography)

####
filmography = pd.DataFrame(columns=['person','credit_type','year','title','imdb_link','episode_count','add_info'])
performers = pd.read_csv("actors.csv")
performers.apply(lambda row: get_person_filmography(performers, row, "imdb_link"), axis=1)

filmography.to_csv("performers_filmography.csv", index=False)
