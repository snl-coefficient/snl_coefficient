import pandas as pd 

all_movies_collected = pd.read_csv("data/running_snl_movies_data.csv",error_bad_lines=False)
all_snl_movies = pd.read_csv("snl_movies_credits.csv")

print(all_movies_collected.shape[0])
print(all_snl_movies.shape[0])
running_list = all_movies_collected['imdb_link'].to_list()
actual_list = all_snl_movies['imdb_link'].to_list()
keep_list = [f for f in running_list if f in actual_list] # only keep those that are currently in all_snl_movies, some things might not end up there
filtered_movies = all_movies_collected[all_movies_collected["imdb_link"].isin(keep_list)]
filtered_movies.to_csv("testing_raw_snl_movies_data.csv", index=False)