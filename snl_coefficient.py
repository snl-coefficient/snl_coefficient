import json
import ssl
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

snl_url = 'https://www.imdb.com/title/tt0072562/'

def get_web_page_content(url):
  req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
  webpage = urlopen(req).read()
  soup = BeautifulSoup(webpage, 'html.parser')
  return soup

def get_extra_details(movie):
  inner_soup = get_web_page_content(movie["imdb_link"])
  div = inner_soup.find('div', attrs={'class':'plot_summary'})
  div_summary = div.find('div', attrs={'class':'summary_text'})
  movie['summary'] = div_summary.text.strip()
  for characters_div in div.findAll('div', attrs={'class':'credit_summary_item'})
    character_data = characters_div.text.strip().split("\n")
    movie[character_data[0][:1]] = character_data[1].replace("|","").strip()
  return(movie)

  def get_top_rated_imdb_hits(url, file_name, nos):
      soup = get_web_page_content(url)
      divs = soup.find('tbody', attrs={'class': 'lister-list'})
      movies = []
      i = 1
      for tr in divs.findAll('tr'):
          movie = {}

links:
https://www.geeksforgeeks.org/scrape-imdb-movie-rating-and-details-using-python/

import re
def getCrewData(url):
    crew_data = {
        "crew": []
    }
    r = requests.get(url=url)

    # Create a BeautifulSoup object
    soup = BeautifulSoup(r.text, 'html.parser')

    #page title
    title = soup.find('title')
    crew_data["title"] = title.string
    cast_list = soup.find("table", {"class" : "cast_list"})

    trows = cast_list.find_all('tr')

    for tr in trows:
        td = tr.find_all('td')
        if len(td)==4:
            row = [i.text for i in td]
            crew_data["crew"].append({
                "name":re.sub("[^a-zA-Z' ]+", '', row[1]).strip(),
                "character":re.sub("[^a-zA-Z' ]+", '', row[3]).strip()
            })
    return crew_data
