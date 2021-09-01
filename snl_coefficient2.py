import requests
from bs4 import BeautifulSoup
import re

snl_url = "https://www.imdb.com/title/tt0072562/"

r = requests.get(url=snl_url)
# create a BeautifulSoup object
soup = BeautifulSoup(r.text, 'html.parser')

#page title
#title = soup.find('title')
#print(title.string)
#data["title"] = title.string

soup.find_all('div')
soup.find("div",{'class':'titleBar'})

def getMovieDetails(url):
    data = {}
    r = requests.get(url=url)
    # Create a BeautifulSoup object
    soup = BeautifulSoup(r.text, 'html.parser')

    #page title
    title = soup.find('title')
    data["title"] = title.string

    # rating
    #ratingValue = soup.find("span", {"itemprop" : "ratingValue"})
    #data["ratingValue"] = ratingValue.string

    # no of rating given
    ratingCount = soup.find("span", {"itemprop" : "ratingCount"})
    data["ratingCount"] = ratingCount.string

    # name
    titleName = soup.find("div",{'class':'titleBar'}).find("h1")
    data["name"] = titleName.contents[0].replace(u'\xa0', u'')

   # additional details
    subtext = soup.find("div",{'class':'subtext'})
    data["subtext"] = ""
    for i in subtext.contents:
        data["subtext"] += i.string.strip()

    # summary
    summary_text = soup.find("div",{'class':'summary_text'})
    data["summary_text"] = summary_text.string.strip()

    credit_summary_item = soup.find_all("div",{'class':'credit_summary_item'})
    data["credits"] = {}
    for i in credit_summary_item:
        item = i.find("h4")
        names = i.find_all("a")
        data["credits"][item.string] = []
        for i in names:
            data["credits"][item.string].append({
                "link": i["href"],
                "name": i.string
            })
    return data

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
    print(trows)

    for tr in trows:
        td = tr.find_all('td')
        if len(td)==4:
            row = [i.text for i in td]
            crew_data["crew"].append({
                "name":re.sub("[^a-zA-Z' ]+", '', row[1]).strip(),
                "character":re.sub("[^a-zA-Z' ]+", '', row[3]).strip()
            })
    return crew_data

getMovieDetails(snl_url)
getCrewData(snl_url)
