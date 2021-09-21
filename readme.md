# scrape SNL cast and crew into a spreadsheet, but need to keep real cast people. need name, imdb link, and
# for each person, scrape their film and TV history using get_extra_details as well as their role in the film (billing)
# for each film, scrape the IMDB show/movie, name, year, ratings, summary, director, writers, stars
#

# Python Scripts 
* **get_imdb_links.py** searches IMDB for the SNL alums and gets the matching link for that individual. 
* **scrape_person_filmography.py** scrapes the IMDB filmography history for each SNL alum and creates **performers_filmography.csv**
* **clean_person_filmography.py** cleans the **performers_filmography.csv** to only include media produced during/after the performers' stint on SNL, and saves it as **performers_filmography_cleaned.csv**, **filmography_credits.csv**, and **person_credits_title.csv**, and **snl_movies_credits.csv**.
* **scrape_movie_data.py** uses the **snl_movie_credits.csv** to scrape the IMDB info for each piece of SNL-related media and saves it as **snl_movies_data.csv**.  
* **calculate_person_coefficient.py**
* **calculate_movie_coefficient.py**
* snl_coefficient.py -- delete?
* snl_coefficient2.py -- delete?

# CSV Files 
* **actors.csv**: person,year_start,year_end,num_seasons,repertory_player,featured_player,middle_group,weekend_update,hosted,best_of,writer,imdb_link,num_featured,num_rep,num_hw
* **writers.csv**: person,year_start,year_end,num_seasons,repertory_player,featured_player,middle_group,weekend_update,hosted,best_of,writer,imdb_link,num_featured,num_rep,num_hw
* **performers_filmography.csv**: person,credit_type,year,title,imdb_link,media_type,total_episode_count,add_info
* **performers_filmography_cleaned**.csv: person,credit_type,year,title,imdb_link,media_type,total_episode_count,add_info,year_start,year_end,keep?
* **person_credits_title.csv**: person,credit_type,title,imdb_link
* **snl_movies_credits.csv**: title,imdb_link,credits_count,snl_alums,cast_count
