from bokeh.plotting import figure, show
import pandas as pd 
from pandas import Series
import os

path = os.getcwd()
path = path.split('/')
path = '/'.join(path[:-1])   

snl_movies = pd.read_csv(f"{path}/data/definitive_snl_movies.csv")
snl_movies['genre-single'] = snl_movies['genres'].str.strip('[]')
snl_movies['genre-single'] = snl_movies['genre-single'].str.strip("'")
snl_movies['genre-single'] = snl_movies['genre-single'].str.split(",")
snl_movies = snl_movies.explode("genre-single").reset_index(drop=True)
snl_movies['genre-single'] = snl_movies['genre-single'].str.strip("'")
snl_movies.to_csv(f"{path}/data/definitive_snl_movies_single_genre.csv", index=False)

genres = list(set(snl_movies['genre-single'].to_list()))
media = list(set(snl_movies['medium'].to_list()))
colors = ["#326f5f", "#5f326f", "#6f5f32","#ffb98c","#3d5d53","#030823","#4e5265","#fff200"]

# dictionary for each medium in which a genre appears
data = snl_movies.groupby(['genre-single', 'medium']).size().reset_index(name="Count")
print(data)

p = figure(x_range=genres, height=250, title="Definitive SNL Movies by Genre and Medium",
           toolbar_location=None, tools="hover", tooltips="$name @genre: @$name")

p.vbar_stack(years, x='genre-single', width=0.1, color=colors, source=data,
             legend_label=media)

p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xgrid.grid_line_color = None
p.axis.minor_tick_line_color = None
p.outline_line_color = None
p.legend.location = "top_left"
p.legend.orientation = "horizontal"

show(p)