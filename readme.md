# scrape SNL cast and crew into a spreadsheet, but need to keep real cast people. need name, imdb link, and
# for each person, scrape their film and TV history using get_extra_details as well as their role in the film (billing)
# for each film, scrape the IMDB show/movie, name, year, ratings, summary, director, writers, stars
#

# Python Scripts 
* **get_imdb_links.py** searches IMDB for the SNL alums and gets the matching link for that individual. 
* **scrape_person_filmography.py** scrapes the IMDB filmography history for each SNL alum and creates **performers_filmography.csv**
* **clean_person_filmography.py** cleans the **performers_filmography.csv** to only include media produced during/after the performers' stint on SNL, and saves it as **performers_filmography_cleaned.csv**, **filmography_credits.csv**, and **person_credits_title.csv**, and **snl_movies_credits.csv**.
* **scrape_movie_data.py** uses the **snl_movie_credits.csv** to scrape the IMDB info for each piece of SNL-related media and saves it as **snl_movies_data.csv**.  
* **person_snl_credit.py** uses the **performers_filmography_cleaned.csv** to create **only_snl_filmography.csv**, which only includes SNL alum info related to *Saturday Night Live* specifically. It then calculates the number of writing and acting credits for each person, adding those columns to **snl_alums.csv**.
* **calculate_person_coefficient.py** uses the **snl_alums.csv** to calculate a coefficient for each person. 
* **calculate_movie_coefficient.py** -- this is not done.
* snl_coefficient.py -- delete?
* snl_coefficient2.py -- delete?

# CSV Files 
* **snl_alums.csv**:person,year_start,year_end,num_seasons_writer,num_seasons_headwriter,num_seasons_actor	num_seasons_rep,num_seasons_featured,num_seasons_middle,num_seasons_weekend_update,num_episodes_weekend_updates,best_of,num_episodes_hosted
* **actors.csv** (*inactive*): person,year_start,year_end,num_seasons,repertory_player,featured_player,middle_group,weekend_update,hosted,best_of,writer,imdb_link,num_featured,num_rep,num_hw
* **writers.csv** (*inactive*): person,year_start,year_end,num_seasons,repertory_player,featured_player,middle_group,weekend_update,hosted,best_of,writer,imdb_link,num_featured,num_rep,num_hw
* **performers_filmography.csv**: person,credit_type,year,title,imdb_link,media_type,total_episode_count,add_info
* **performers_filmography_cleaned**.csv: person,credit_type,year,title,imdb_link,media_type,total_episode_count,add_info,year_start,year_end,keep?
* **person_credits_title.csv**: person,credit_type,title,imdb_link
* **snl_movies_credits.csv**: title,imdb_link,credits_count,snl_alums,cast_count
