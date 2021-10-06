import pandas as pd 
import csv 

####
snl_movie_credits = pd.read_csv("snl_movies_credits.csv")
snl_movie_data = pd.read_csv("snl_movies_data.csv")
person_credits_title = pd.read_csv("person_credits_title.csv")
snl_movie_credits['movie_coefficient'] = ''
performers = pd.read_csv("performers_with_coefficient.csv")

snl_coefficients = {}
snl_coefficients = performers.set_index('person').to_dict()['coefficient']

snl_films = ['https://www.imdb.com/title/tt0080455/',"https://www.imdb.com/title/tt0105793/",'https://www.imdb.com/title/tt0106598/',"https://www.imdb.com/title/tt0108525/","https://www.imdb.com/title/tt0110169/",'https://www.imdb.com/title/tt0114571/','https://www.imdb.com/title/tt0118747/','https://www.imdb.com/title/tt0120770/','https://www.imdb.com/title/tt0167427/','https://www.imdb.com/title/tt0213790/','https://www.imdb.com/title/tt1470023/','https://www.imdb.com/title/tt3677742/','https://www.imdb.com/title/tt3461424/','https://www.imdb.com/title/tt1315217/','https://www.imdb.com/title/tt9881938/','https://www.imdb.com/title/tt1899280/','https://www.imdb.com/title/tt1577870/','https://www.imdb.com/title/tt0896972/','https://www.imdb.com/title/tt1217217/','https://www.imdb.com/title/tt4460266/','https://www.imdb.com/title/tt1635658/','https://www.imdb.com/title/tt0435730/','https://www.imdb.com/title/tt0818577/','https://www.imdb.com/title/tt0500149/','https://www.imdb.com/title/tt1276981/','https://www.imdb.com/title/tt0301807/','https://www.imdb.com/title/tt0896971/','https://www.imdb.com/title/tt1003289/','https://www.imdb.com/title/tt1152284/','https://www.imdb.com/title/tt0332374/','https://www.imdb.com/title/tt0896970/','https://www.imdb.com/title/tt0500191/','https://www.imdb.com/title/tt0344303/','https://www.imdb.com/title/tt0500100/','https://www.imdb.com/title/tt0196072/','https://www.imdb.com/title/tt0448725/','https://www.imdb.com/title/tt0489269/','https://www.imdb.com/title/tt0255575/','https://www.imdb.com/title/tt0274793/','https://www.imdb.com/title/tt0276469/','https://www.imdb.com/title/tt2203885/','https://www.imdb.com/title/tt0255576/','https://www.imdb.com/title/tt0266934/','https://www.imdb.com/title/tt0500148/','https://www.imdb.com/title/tt0424406/','https://www.imdb.com/title/tt0899167/','https://www.imdb.com/title/tt1093390/','https://www.imdb.com/title/tt0500163/','https://www.imdb.com/title/tt0498994/','https://www.imdb.com/title/tt1093389/','https://www.imdb.com/title/tt0272826/','https://www.imdb.com/title/tt1045653/','https://www.imdb.com/title/tt0814302/','https://www.imdb.com/title/tt0274795/','https://www.imdb.com/title/tt6947028/','https://www.imdb.com/title/tt4873968/','https://www.imdb.com/title/tt6354260/','https://www.imdb.com/title/tt0424407/','https://www.imdb.com/title/tt1613125/','https://www.imdb.com/title/tt13465928/','https://www.imdb.com/title/tt13465912/','https://www.imdb.com/title/tt0255573/','https://www.imdb.com/title/tt0255574/','https://www.imdb.com/title/tt1094580/','https://www.imdb.com/title/tt1537895/','https://www.imdb.com/title/tt4240752/','https://www.imdb.com/title/tt0773307/','https://www.imdb.com/title/tt3407988/','https://www.imdb.com/title/tt2963280/','https://www.imdb.com/title/tt1417590/','https://www.imdb.com/title/tt0478824/','https://www.imdb.com/title/tt0433447/','https://www.imdb.com/title/tt0433446/','https://www.imdb.com/title/tt0477851/','https://www.imdb.com/title/tt0487269/','https://www.imdb.com/title/tt0382275/','https://www.imdb.com/title/tt0486767/','https://www.imdb.com/title/tt4873938/','https://www.imdb.com/title/tt11306452/','https://www.imdb.com/title/tt6548600/','https://www.imdb.com/title/tt4453228/','https://www.imdb.com/title/tt3377584/','https://www.imdb.com/title/tt3325974/','https://www.imdb.com/title/tt1452923/','https://www.imdb.com/title/tt0462518/','https://www.imdb.com/title/tt0769773/','https://www.imdb.com/title/tt0274794/','https://www.imdb.com/title/tt5470146/','https://www.imdb.com/title/tt1763321/','https://www.imdb.com/title/tt3513114/','https://www.imdb.com/title/tt0337712/','https://www.imdb.com/title/tt0331625/','https://www.imdb.com/title/tt0390445/','https://www.imdb.com/title/tt0426384/','https://www.imdb.com/title/tt3709798/','https://www.imdb.com/title/tt7646120/','https://www.imdb.com/title/tt14325040/','https://www.imdb.com/title/tt1566615/','https://www.imdb.com/title/tt6545172/','https://www.imdb.com/title/tt4416816/','https://www.imdb.com/title/tt4460272/','https://www.imdb.com/title/tt2591712/']

for index, row in snl_movie_data.iterrows():
    # gets SNL-related information from the snl_movie_credits
    imdb_link = snl_movie_credits['imdb_link'].values[index]
    credits_count = snl_movie_credits['credits_count'].values[index]
    cast_count = snl_movie_credits['cast_count'].values[index]
    snl_alums = snl_movie_credits['snl_alums'].values[index]
    person_values = []
    # get IMDB information from snl_movie_data 
    movie_info = snl_movie_data[snl_movie_data['imdb_link']==imdb_link]
    #cast = movie_info['stars'].values[index]
    principal_people = movie_info['principal_people'].values[index]
    num_episodes = int(float(movie_info['num_episodes'].values[index]))
    #print(num_episodes)
    # create a dataframe of the roles strictly for that movie 
    pct = person_credits_title[person_credits_title['imdb_link']==imdb_link]
    pct.to_csv("filtered_movie_credits_storage.csv", index=False)
    movie_roles = pd.read_csv("filtered_movie_credits_storage.csv")
    # now iterate over the roles dataframe
    for index, row in movie_roles.iterrows():
        person = movie_roles['person'].values[index]
        person_role = movie_roles['credit_type'].values[index]
        person_num_episodes = int(float(movie_roles['total_episode_count'].values[index]))
        if num_episodes != 0:
            print(person_num_episodes)
            print(num_episodes)
            percent_episodes = person_num_episodes/num_episodes
        else: 
            percent_episodes = 1
        person_coefficient = snl_coefficients.get(person)
        if person in principal_people:
            role_coefficient = 2
            value = person_coefficient * role_coefficient * percent_episodes
        elif person_role == 'producer':
                role_coefficient = 2
                value = person_coefficient * role_coefficient * percent_episodes
        else:
            value = person_coefficient * percent_episodes
        person_values.append(value)
    sum_of_values= sum(person_values)
    if imdb_link in snl_films: 
        sum_of_values += 5
    movie_coefficient = sum_of_values/cast_count
    snl_movie_data.at[index,"movie_coefficient"] = movie_coefficient
    
snl_movie_data.to_csv("snl_movie_coefficient.csv", index=False)

