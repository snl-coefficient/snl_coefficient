import pandas as pd 
import itertools 
import collections
from itertools import combinations 
import os

path = os.getcwd()
path = path.split('/')
path = '/'.join(path[:-1])
    
snl_movie_data = pd.read_csv(f"{path}/data/full_data_snl_movies_coefficient.csv")
alums_count['snl_alums'] = alums_count['snl_alums'].apply(eval)
pairs_list = []
for index, row in snl_movie_data.iterrows():
    snl_alums = snl_movie_data['snl_alums'].values[index]
    snl_alums.sort()
    pairs = list(combinations(list_snl_alums, 2))
    for pair in pairs: 
        pairs_list.append(pair)
frequencyDict = collections.Counter(pairs_list)
pairs_frequency = pd.DataFrame.from_dict(frequencyDict, orient='index').reset_index()
pairs_frequency.rename(columns={'index':'relationship', 0:'count'}, inplace=True)
#pairs_frequency[['source', 'target']] = pairs_frequency['relationship'].str.split(",", 1, expand=True) - still need to split
pairs_frequency.to_csv(f"{path}/data/pairs_frequency.csv", index=False)