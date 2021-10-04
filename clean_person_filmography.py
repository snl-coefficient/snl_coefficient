import json
import ssl
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urlencode
import urllib
import numpy as np
import re
from string import digits

####
def get_crew_list(dataframe, row):
    try:
        movie = dataframe['imdb_link'].values[row.name]
        title = dataframe['title'].values[row.name]
        movie_df = dataframe[dataframe['imdb_link'] == movie]
        cast_list = set(movie_df['person'].tolist())
        dataframe.at[row.name,'snl_alums'] = cast_list 
        dataframe.at[row.name,'snl_alums_count'] = len(cast_list) 
        #print(title, cast_list, len(cast_list))
    except:
        pass

def filter_out_start_year(dataframe, dict1, dict2, column):
    for index, row in dataframe.iterrows():
        person = dataframe["person"].values[index]
        title = dataframe["title"].values[index]
        movie_year_start = int(dataframe["year_start"].values[index])
        movie_year_end = int(dataframe["year_end"].values[index])
        performer_year_start = dict1.get(person)
        performer_year_end = dict2.get(person)
        print(person, title, movie_year_start, movie_year_end, performer_year_start, performer_year_end)
        if int(movie_year_start) > int(performer_year_start):
            dataframe.at[index,column]= "keep_year"
        elif int(movie_year_end) > int(performer_year_end):
            dataframe.at[index,column]= "keep_year"
        elif int(movie_year_start) == int(performer_year_start):
            dataframe.at[index,column]= "keep_year"
        elif int(movie_year_end) == int(performer_year_end):
            dataframe.at[index,column]= "keep_year"
        else:
            dataframe.at[index,column]= "no_keep"

def filter_out_credit_types(dataframe, row, column):
    credit_type = dataframe["credit_type"].values[row.name]
    credit_type = credit_type.split("-")[0]
    interesting_credits = ['writer','director','producer','actor','actress','self','archive_footage']
    for role in interesting_credits:
        if credit_type.startswith(role):
            dataframe.at[row.name,column]= "keep_credit"
            dataframe.at[row.name,"credit_type"] = credit_type
        else:
            pass

def add_end_years(dataframe, row, column):
    dates = dataframe[column].values[row.name]
    dates = str(dates).strip()
    if "-" in dates:
        if dates.endswith("-"):
            new_dates = str(dates) + "2021" #end year 
            dataframe.at[row.name, column] = new_dates
    else:
        dataframe.at[row.name, column] = dates + "-" + dates
        
def fill_all_years(dataframe, row):
  year_start = dataframe['year_start'].values[row.name]
  year_start = year_start.strip()
  year_end = dataframe['year_end'].values[row.name]
  year_end = year_end.strip()
  if year_start == 'nan': # for rows where year_start is blank? or 'NaN' - gotta figure out what it's called 
    if year_end == 'nan': # for rows where year_end is blank 
      media_type = dataframe['media_type'].values[row.name]
      media_type = media_type.split(' ')
      revised_list = []
      for item in media_type:
        item = item.strip()
        non_number = re.compile(r'[^\d]+')
        new_item = non_number.sub('',item)
        new_item = re.sub('[()]', '', new_item)
        revised_list.append(new_item)
      revised_list = [x.strip() for x in revised_list if x.strip()]
      revised_list = [i for i in revised_list if i]
      only_numbers = []
      for item in revised_list:
        if len(item) == 4:
            item = int(item)
            only_numbers.append(item)
      if len(only_numbers) != 0:
          dataframe.at[row.name,'year_start'] = str(min(only_numbers))
          dataframe.at[row.name,'year_end'] = str(max(only_numbers))

#######
performers = pd.read_csv("snl_alums.csv")
filmography_orig = pd.read_csv("performers_filmography.csv")

print("adding end and start years")
filmography_orig.apply(lambda row: add_end_years(filmography_orig, row, 'year'), axis=1)
filmography_orig[['year_start','year_end']] = filmography_orig['year'].str.split("-",expand=True)
filmography_orig.apply(lambda row: fill_all_years(filmography_orig, row), axis=1)
cols_to_change = ['year_start', "year_end"]
for col in cols_to_change:
    filmography_orig[col] = filmography_orig[col].str.extract('(\d+)')
filmography_orig['keep?'] = ''
cols_to_keep = ['person','credit_type','title','imdb_link','total_episode_count','year_start','year_end','keep?']
filmography = filmography_orig.filter(items=cols_to_keep)

print("filtering out credits")
filmography_credits = filmography_orig.copy(deep=True)
print("number of filmography credits: ", filmography_credits.shape[0])
filmography_credits.apply(lambda row: filter_out_credit_types(filmography_credits, row, 'keep?'), axis=1)
filmography_credits = filmography_credits[filmography_credits['keep?']=='keep_credit']
filmography_credits = filmography_credits[filmography_credits['year_start'] != 'nan']
filmography_credits.to_csv("filmography_credits.csv", index=False)
print("number of filmography credits: ", filmography_credits.shape[0])

snl_starts = {}
snl_starts = performers.set_index('person').to_dict()['year_start']
print(snl_starts)

snl_ends = {}
snl_ends = performers.set_index('person').to_dict()['year_end']

filmography_years = filmography_credits.copy(deep=True)

filmography_years["year_start"] = pd.to_numeric(filmography_years["year_start"], errors='coerce').fillna(0)
filmography_years["year_end"] = pd.to_numeric(filmography_years["year_end"], errors='coerce').fillna(0)
filmography_years[["year_start", "year_end"]] = filmography_years[["year_start", "year_end"]].apply(pd.to_numeric)
filmography_years[["year_start", "year_end"]] = filmography_years[["year_start", "year_end"]].astype(int)
filmography_years.drop('keep?', axis=1, inplace=True)

print("filtering out start years")
filmography_years['keep?'] = ''
filmography_years  =filmography_years.reset_index(drop=True) 
filter_out_start_year(filmography_years, snl_starts, snl_ends, 'keep?')
filmography_cleaned = filmography_years[filmography_years['keep?']=='keep_year']
filmography_cleaned['imdb_link'] = filmography_cleaned['imdb_link'].str.split("?").str[0]
filmography_cleaned.to_csv("performers_filmography_cleaned.csv", index=False)
print("number of filmography credits: ", filmography_cleaned.shape[0])

cols_to_keep = ['person','credit_type','media_type','title','imdb_link']
filmography = filmography_cleaned.filter(items=cols_to_keep)
filmography.to_csv("person_credits_title.csv", index=False)

filmography['snl_alums'] = ''
filmography['credits_count'] = ''
filmography['snl_alums_count'] = ''
filmography['credits_count'] = filmography.groupby('imdb_link')['imdb_link'].transform('count')

cast_df = pd.DataFrame({'imdb_link':filmography.imdb_link.unique()})
cast_df['snl_alums'] = [list(set(filmography['person'].loc[filmography['imdb_link'] == x['imdb_link']])) for _, x in cast_df.iterrows()]
cast_df['cast_count'] = cast_df['snl_alums'].str.len()

cols_to_keep = ['title','media_type','imdb_link','credits_count','cast_count']
filmography= filmography.filter(items=cols_to_keep)
filmography = filmography.drop_duplicates(subset="imdb_link")

filmography_done = pd.merge(filmography, cast_df, on="imdb_link", how="outer")
print("number of filmography credits: ", filmography_done.shape[0])
filmography_done.to_csv("snl_movies_credits.csv", index=False)