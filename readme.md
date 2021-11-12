# SNL Coefficient 
## To Do List 
- Finish the calculate_movie_coefficient
- Fix the principal_people scraping section 
- Need to be able to generate media_types.txt and genres.txt

This repository contains all the scripts and data for the SNL Coefficient project. This project attempts to determine a value for cast and crew members' association with *Saturday Night Live*, to then determine how closely associated a particular media property is with the show. 

For the purposes of this project, cast and crew applies to 1) repertory players, 2) featured players, 3) staff writers, and 4) head writers, during the show's period. Data for the **snl_cast_crew.csv** has been collected from Wikipedia, IMDB, and fan sources. 

The Python scripts can be run in the order listed below to complete the project. 

## Python Scripts 
* **get_imdb_links.py** searches Internet Movie Database (IMDB) for the *Saturday Night Live* alums listed in **snl_cast_crew.csv** and updates with the matching link for each individual. The SNL alum names are listed as they would be on IMDB, not as they may have been credited on *Saturday Night Live* (Jim Downey is listed as "James Downey (I)").  
* **scrape_person_filmography.py** scrapes the IMDB filmography history for each SNL alum using **snl_alums.csv** and creates **performers_filmography.csv**
* **clean_person_filmography.py** cleans **performers_filmography.csv** to only include media produced during/after the performers' stint on SNL, and saves it as **performers_filmography_cleaned.csv**, **filmography_credits.csv**, and **person_credits_title.csv**, and **snl_movies_credits.csv**.
* **person_snl_credits.py** uses **performers_filmography_cleaned.csv** to create **only_snl_filmography.csv**, which only includes SNL alum info related to *Saturday Night Live* specifically. It then calculates the number of episodes with writing and acting credits for each person, adding those columns to **snl_alums.csv**.
* **calculate_person_coefficient.py** uses **snl_alums.csv** to calculate a coefficient for each person and saves it as a column in **performers_with_coefficient.csv**. 
* **scrape_movie_data.py** uses **snl_movies_credits.csv** to scrape the IMDB info for each piece of SNL-related media and saves it as **snl_movies_data.csv**. This script has a time delay of 2 seconds between scraping, and if it reaches any type of error (typically a 500 Internal Service Error) it pauses for 1000 seconds. 
* **clean_movie_data.py** uses **snl_movies_data.csv** to clean for the media type and year information and saves it as **cleaned_snl_movies_data.csv**. 
* **calculate_movie_coefficient.py** uses **snl_movie_credits.csv**, **cleaned_snl_movie_data.csv**, **person_credits_title.csv**, and **performers_with_coefficient.csv** to calculate the movie coefficient, and saves it as a column in **full_data_snl_movie_coefficient.csv**.

## CSV Files 
* **snl_alums.csv**:person,year_start,year_end,num_seasons_writer,num_seasons_headwriter,num_seasons_actor	num_seasons_rep,num_seasons_featured,num_seasons_middle,num_seasons_weekend_update,num_episodes_weekend_updates,best_of,num_episodes_hosted
* **performers_filmography.csv**: person,credit_type,year,title,imdb_link,media_type,total_episode_count,add_info
* **performers_filmography_cleaned**.csv: person,credit_type,year,title,imdb_link,media_type,total_episode_count,add_info,year_start,year_end,keep?
* **person_credits_title.csv**: person,credit_type,title,imdb_link
* **snl_movies_credits.csv**: title,imdb_link,credits_count,snl_alums,cast_count
* **only_snl_filmography.csv**: person,credit_type,year,title,imdb_link,media_type,total_episode_count,add_info,year_start,year_end,keep?
* **performers_with_coefficient.csv**:person,year_start,year_end,num_seasons_total,num_seasons_writer,num_seasons_headwriter,num_seasons_actor,num_seasons_rep,num_seasons_featured,num_seasons_middle,num_seasons_weekend_update,num_episodes_weekend_updates,best_of,num_episodes_hosted,imdb_link,num_episodes_writer,num_episodes_actor,num_epsiodes_actor,num_epsiodes_writer,coefficient,num_episodes_other
* **person-title-imdb_link.csv**: person,title,imdb_link
* **raw_snl_movies_data.csv**: title,media_type,imdb_link,credits_count,snl_alums,cast_count,genres,stars,num_episodes,principal_people,production_companies
* **running_snl_movies_data.csv**:imdb_link,genres,stars,media_type,num_episodes,principal_people,production_companies 
* **cleaned_snl_movies_data.csv**: imdb_link,genres,stars,media_type,num_episodes,principal_people,production_companies,medium,year_start,year_end

* **snl_movies_coefficient.csv**:imdb_link,genres,stars,media_type,num_episodes,principal_people,production_companies,medium,year_start,year_end,movie_coefficient
**full_data_snl_movie_coefficient.csv**: imdb_link,movie_coefficient_x,title,media_type_x,credits_count,snl_alums,cast_count,genres,stars,media_type_y,num_episodes,principal_people,production_companies,medium,year_start,year_end,movie_coefficient_y

## Other Files 
* **production_companies.txt**: a list of all the production companies that have produced SNL-related media
* **mediums.txt**: a list of all the media forms (TV Series, TV Special, Podcast Series, etc.) as well as ratings (R, PG-13, TV-14, etc.) represented in SNL-related media 
* **snl_alums.txt** - should make in the first script 
* **genres.txt**: a list of all the genres represented in SNL-related media. 