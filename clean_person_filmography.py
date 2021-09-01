import json
import ssl
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urlencode
import urllib
import numpy as np

def get_crew_list(dataframe, row):
    try:
        movie = dataframe['imdb_link'].values[row.name]
        title = dataframe['title'].values[row.name]
        movie_df = dataframe[dataframe['imdb_link'] == movie]
        cast_list = set(movie_df['person'].tolist())
        dataframe.at[row.name,'snl_alums'] = cast_list 
        dataframe.at[row.name,'snl_alums_count'] = len(cast_list) 
        print(title, cast_list, len(cast_list))
    except:
        pass

def filter_out_start_year(dataframe, row, dict1, dict2, column):
    try:
        person = dataframe["person"].values[row.name]
        movie_year_start = dataframe["year_start"].values[row.name]
        movie_year_end = dataframe["year_end"].values[row.name]
        performer_year_start = dict1.get(person)
        performer_year_end = dict2.get(person)
        if isinstance(movie_year_start, float):
            pass
        elif int(movie_year_start) >= int(performer_year_start):
            dataframe.at[row.name,column]= "keep_year"
        elif not isinstance(movie_year_end, int):
            pass
        elif int(movie_year_end) >= int(performer_year_end):
            dataframe.at[row.name,column]= "keep_year"
        else:
            pass
    except:
        pass

def filter_out_credit_types(dataframe, row, column):
    credit_type = dataframe["credit_type"].values[row.name]
    credit_type = credit_type.split("-")[0]
    interesting_credits = ['writer','director','producer','actor','actress','self']
    for role in interesting_credits:
        if credit_type.startswith(role):
            dataframe.at[row.name,column]= "keep_credit"
            dataframe.at[row.name,"credit_type"] = credit_type
        else:
            pass

#######
performers = pd.read_csv("actors.csv")
filmography_orig = pd.read_csv("performers_filmography.csv")
filmography_orig[['year_start','year_end']] = filmography_orig['year'].str.split("-",expand=True)
cols_to_change = ['year_start', "year_end"]
for col in cols_to_change:
    filmography_orig[col] = filmography_orig[col].str.extract('(\d+)')
filmography_orig['keep?'] = ''

filmography_credits = filmography_orig.copy(deep=True)
print(filmography_credits.shape[0])
#filmography_credits.drop(filmography_credits.tail(1).index,inplace = True)
filmography_credits.apply(lambda row: filter_out_credit_types(filmography_credits, row, 'keep?'), axis=1)
filmography_credits = filmography_credits[filmography_credits['keep?']=='keep_credit']

snl_starts = {}
snl_starts = performers.set_index('person').to_dict()['year_start']

snl_ends = {}
snl_ends = performers.set_index('person').to_dict()['year_end']

filmography_years = filmography_credits.copy(deep=True)

filmography_years['year_start'] = filmography_years['year_start'].replace(np.nan, 0)
filmography_years['year_end'] = filmography_years['year_end'].replace(np.nan, 0)
filmography_years["year_start"] = pd.to_numeric(filmography_years["year_start"], errors='coerce').fillna(0)
filmography_years["year_end"] = pd.to_numeric(filmography_years["year_end"], errors='coerce').fillna(0)
filmography_years[["year_start", "year_end"]] = filmography_years[["year_start", "year_end"]].apply(pd.to_numeric)
filmography_years[["year_start", "year_end"]] = filmography_years[["year_start", "year_end"]].fillna(0)
filmography_years[["year_start", "year_end"]] = filmography_years[["year_start", "year_end"]].replace('NaN',0)
filmography_years[["year_start", "year_end"]] = filmography_years[["year_start", "year_end"]].astype(int)

filmography_years.apply(lambda row: filter_out_start_year(filmography_years, row, snl_starts, snl_ends, 'keep?'), axis=1)
filmography_cleaned = filmography_years[filmography_years['keep?']=='keep_year']
filmography_cleaned['imdb_link'] = filmography_cleaned['imdb_link'].str.split("?").str[0]
filmography_cleaned.to_csv("performers_filmography_cleaned.csv", index=False)

cols_to_keep = ['person','credit_type','title','imdb_link']
filmography = filmography_cleaned.filter(items=cols_to_keep)
filmography.to_csv("person_credits_title.csv", index=False)

filmography['snl_alums'] = ''
filmography['credits_count'] = ''
filmography['snl_alums_count'] = ''
filmography['credits_count'] = filmography.groupby('imdb_link')['imdb_link'].transform('count')
filmography.to_csv("cast_count.csv", index=False)


cast_df = pd.DataFrame({'imdb_link':filmography.imdb_link.unique()})
cast_df['snl_alums'] = [list(set(filmography['person'].loc[filmography['imdb_link'] == x['imdb_link']])) for _, x in cast_df.iterrows()]
#cast_df['cast_count'] = cast_df.snl_alums.str.len().sum()
cast_df['cast_count'] = cast_df['snl_alums'].str.len()
cast_df.to_csv("cast_df.csv", index=True)

cols_to_keep = ['title','imdb_link','credits_count','cast_count']
filmography= filmography.filter(items=cols_to_keep)
filmography = filmography.drop_duplicates(subset="imdb_link")

filmography_done = pd.merge(filmography, cast_df, on="imdb_link", how="outer")
filmography_done.to_csv("snl_movies_credits.csv", index=False)