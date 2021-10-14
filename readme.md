# scrape SNL cast and crew into a spreadsheet, but need to keep real cast people. need name, imdb link, and
# for each person, scrape their film and TV history using get_extra_details as well as their role in the film (billing)
# for each film, scrape the IMDB show/movie, name, year, ratings, summary, director, writers, stars
#

# Python Scripts 
* **get_imdb_links.py** searches IMDB for the SNL alums listed in **snl_alums.csv** and updates with the matching link for each individual. The SNL alum names are listed as they would be on IMDB, not as they may have been credited on *Saturday Night Live* (Jim Downey is listed as "James Downey (I)").  
* **scrape_person_filmography.py** scrapes the IMDB filmography history for each SNL alum using **snl_alums.csv** and creates **performers_filmography.csv**
* **clean_person_filmography.py** cleans **performers_filmography.csv** to only include media produced during/after the performers' stint on SNL, and saves it as **performers_filmography_cleaned.csv**, **filmography_credits.csv**, and **person_credits_title.csv**, and **snl_movies_credits.csv**.
* **person_snl_credits.py** uses **performers_filmography_cleaned.csv** to create **only_snl_filmography.csv**, which only includes SNL alum info related to *Saturday Night Live* specifically. It then calculates the number of episodes with writing and acting credits for each person, adding those columns to **snl_alums.csv**.
* **calculate_person_coefficient.py** uses **snl_alums.csv** to calculate a coefficient for each person and saves it as a column in **performers_with_coefficient.csv**. 
* **scrape_movie_data.py** uses **snl_movies_credits.csv** to scrape the IMDB info for each piece of SNL-related media and saves it as **snl_movies_data.csv**. This script has a time delay of 2 seconds between scraping, and also saves to **active-movie-data-scrape.csv** while the script runs in case it crashes. (This script takes a LONG time to run properly - days? It can be stopped at any time and pick up where it left off on the **active-movie-data-scrape.csv**.)
* **clean_movie_data.py** uses **snl_movie_data.csv** to clean for the media type and year information and saves it as **cleaned_snl_movie_data.csv**. 
* **calculate_movie_coefficient.py** uses **snl_movie_credits.csv**, **cleaned_snl_movie_data.csv**, **person_credits_title.csv**, and **performers_with_coefficient.csv** to calculate the movie coefficient, and saves it as a column in **snl_movie_coefficient.csv**.

# CSV Files 
* **snl_alums.csv**:person,year_start,year_end,num_seasons_writer,num_seasons_headwriter,num_seasons_actor	num_seasons_rep,num_seasons_featured,num_seasons_middle,num_seasons_weekend_update,num_episodes_weekend_updates,best_of,num_episodes_hosted
* **actors.csv** (*inactive*): person,year_start,year_end,num_seasons,repertory_player,featured_player,middle_group,weekend_update,hosted,best_of,writer,imdb_link,num_featured,num_rep,num_hw
* **writers.csv** (*inactive*): person,year_start,year_end,num_seasons,repertory_player,featured_player,middle_group,weekend_update,hosted,best_of,writer,imdb_link,num_featured,num_rep,num_hw
* **performers_filmography.csv**: person,credit_type,year,title,imdb_link,media_type,total_episode_count,add_info
* **performers_filmography_cleaned**.csv: person,credit_type,year,title,imdb_link,media_type,total_episode_count,add_info,year_start,year_end,keep?
* **person_credits_title.csv**: person,credit_type,title,imdb_link
* **snl_movies_credits.csv**: title,imdb_link,credits_count,snl_alums,cast_count
* **only_snl_filmography.csv**: person,credit_type,year,title,imdb_link,media_type,total_episode_count,add_info,year_start,year_end,keep?
* **performers_with_coefficient.csv**:person,year_start,year_end,num_seasons_total,num_seasons_writer,num_seasons_headwriter,num_seasons_actor,num_seasons_rep,num_seasons_featured,num_seasons_middle,num_seasons_weekend_update,num_episodes_weekend_updates,best_of,num_episodes_hosted,imdb_link,num_episodes_writer,num_episodes_actor,num_epsiodes_actor,num_epsiodes_writer,coefficient,num_episodes_other
* **person-title-imdb_link.csv**: person,title,imdb_link
* **raw_snl_movie_data.csv**: 
* **running_snl_movies_data.csv**: 
* **cleaned_snl_movie_data.csv**
* **snl_movie_coefficient.csv**:
