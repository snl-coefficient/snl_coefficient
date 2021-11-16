# from here: https://github.com/bokeh/bokeh/tree/branch-3.0/examples/app/movies

from os.path import dirname, join
import numpy as np
import pandas as pd
from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Div, Select, Slider, TextInput
from bokeh.plotting import figure

movies = pd.read_csv("full_data_snl_movies_coefficient.csv")
print(len(movies))
snl_cast_crew = pd.read_csv("snl_cast_crew.csv")
snl_alums_list = snl_cast_crew['person'].to_list().sort()
snl_alums_list.append("All")
snl_media = open(join(dirname(__file__), 'data/snl_media.txt')).read().split()
movies["color"] = "grey"
movies.loc[movies.imdb_link.isin(snl_media), "color"] = "purple"
movies["alpha"] = 1

axis_map = {
    "SNL Coefficient": "movie_coefficient",
    "Year (Start)": "year_start",
}

desc = Div(text=open(join(dirname(__file__), "description.html")).read(), sizing_mode="stretch_width")

# Create Input controls
min_coefficient = Slider(title="Minimum coefficient", value=0, start=0, end=20, step=.01) 
cast_count = Slider(title="Minimum number of SNL alums", value=2, start=2, end=100, step=1)
min_year = Slider(title="Year released", start=1975, end=2022, value=1970, step=1)
max_year = Slider(title="End Year released", start=1975, end=2022, value=2022, step=1)
genre = Select(title="Genre", value="All",
               options=open(join(dirname(__file__), 'data/genres.txt')).read().split()) # create a list of these 
medium = Select(title="Medium", value="All",
               options=[i.strip() for i in open("data/media_types.txt").readlines()]) 
snl_alumni = Select(title="SNL Alum", value="All", options=snl_alums_list)
               
x_axis = Select(title="X Axis", options=sorted(axis_map.keys()), value="Year (Start)")
y_axis = Select(title="Y Axis", options=sorted(axis_map.keys()), value="SNL Coefficient")

source = ColumnDataSource(data=dict(x=[], y=[], color=[], title=[], year=[], alpha=[]))

TOOLTIPS=[
    ("Title", "@title"),
    ("Year (Start)", "@year_start"),
    ("Genre", "@genres"),
    ("Medium", "@medium"),
    ("Cast Count", "@cast_count"),
    ("Coefficient", "@movie_coefficient")
]

p = figure(height=600, width=700, title="", toolbar_location=None, tooltips=TOOLTIPS, sizing_mode="scale_both")
p.circle(x="x", y="y", source=source, size=7, color="color", line_color=None, fill_alpha="alpha")


def select_movies():
    genre_val = genre.value
    medium_val = medium.value
    snl_alumni_val = snl_alumni.value
    print(len(movies))
    selected = movies[
        (movies.year_start >= min_year.value) &
        (movies.year_end <= max_year.value) &
        (movies.movie_coefficient >= min_coefficient.value) &
        (movies.cast_count >= cast_count.value)
        ]
    print("len selected")
    print(len(selected))
    if (genre_val != "All"):
        selected = selected[selected.genres.str.contains(genre_val)==True]
    if (medium_val != "All"):
        selected = selected[selected.medium.str.contains(medium_val)==True]
    if (snl_alumni_val != "All"):
        selected = selected[selected.snl_alums.str.contains(snl_alumni_val)==True]
    return selected


def update():
    df = select_movies()
    x_name = axis_map[x_axis.value]
    y_name = axis_map[y_axis.value]
    p.xaxis.axis_label = x_axis.value
    p.yaxis.axis_label = y_axis.value
    p.title.text = "%d movies selected" % len(df)
    source.data = dict(
        x=df[x_name],
        y=df[y_name],
        color=df["color"],
        cast_count=df["cast_count"],
        title=df["title"],
        year_start=df["year_start"],
        alpha=df["alpha"],
        movie_coefficient=df["movie_coefficient"],
        medium=df["medium"],
        genres=df["genres"]
    )

controls = [genre, medium, cast_count, min_year, snl_alumni, min_coefficient, x_axis, y_axis]
for control in controls:
    control.on_change('value', lambda attr, old, new: update())

inputs = column(*controls, width=320)

l = column(desc, row(inputs, p), sizing_mode="scale_both")

update()  # initial load of the data

curdoc().add_root(l)
curdoc().title = "Movies"