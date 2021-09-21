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

filmography = pd.read_csv("performers_filmography_cleaned.csv")
snl_credits = filmography[filmography["title"]=="Saturday Night Live"]
snl_credits.to_csv("only_snl_filmography.csv")
snl_credits = pd.read_csv("only_snl_filmography.csv")

actors = pd.read_csv("actors.csv")
actors['num_episodes_writer'] = ''
actors['num_episodes_actor'] = ''

def get_snl_counts(dataframe, row):
    person = dataframe['person'].values[row.name]
    num_episodes_actor = 0
    num_episodes_writer = 0
    actor_credit = snl_credits[(snl_credits['person']==person) & (snl_credits['credit_type']=='actor')]
    #print(actor_credit)
    if actor_credit.shape[0] == 0:
        actor_credit = snl_credits[(snl_credits['person']==person) & (snl_credits['credit_type']=='actress')]
    if actor_credit.shape[0] != 0:
        list = actor_credit["total_episode_count"].tolist()
        num_episodes_actor = list[0]
    writer_credit = snl_credits[(snl_credits['person']==person) & (snl_credits['credit_type']=='writer')] #can i change all these values in performers_filmography_cleaned?
    if writer_credit.shape[0] != 0:
        list = writer_credit["total_episode_count"].tolist()
        num_episodes_writer = list[0]
    dataframe.at[row.name,'num_epsiodes_actor'] = num_episodes_actor	
    dataframe.at[row.name,'num_epsiodes_writer'] = num_episodes_writer
    print(person, num_episodes_actor, num_episodes_writer)		
    
actors.apply(lambda row: get_snl_counts(actors, row), axis=1)
actors.to_csv("actors_with_snl_credits.csv", index=False)
