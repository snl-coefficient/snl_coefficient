for index, row in snl_movie_credits.iterrows():
    imdb_link = snl_movie_credits['imdb_link'].values[index]
    movie_roles = performers_filmography_cleaned[performers_filmography_cleaned['imdb_link'] == imdb_link]
    cast_count = snl_movie_credits['cast_count'].values[index]
    cast_count = len(cast_count)
    person_values = []
    movie_info = snl_movie_data[snl_movie_data['imdb_link']== imdb_link]
    cast = movie_info['cast'].values[0]
    creator = movie_info['creator'].values[0]
    director = movie_info['director'].values[0]
    producer = movie_info['producer'].values[0]
    num_episdoes = movie_info['num_episodes'].values[0]
    for index, row in movie_roles.iterrows():
        person_role = movie_roles['role'].values[index]
        person = movie_roles['person'].values[index]
        person_num_episodes = movie_roles['num_episodes'].values[index] # how do i calculate this
        episodes = person_num_episodes/num_episodes
        person_coefficient = snl_coefficients.get(person)
        role_coefficient = roles.get(person_role)
        if person in cast or creator or director or producer:
            role_coefficient +=1
        value = person_coefficient * role_coefficient * num_epsiodes
        person_values.append(value)
    sum_of_values= sum(person_values)
    cast_value = sum_of_values/cast_count


####
snl_coefficients = {}
snl_coefficients = performers.set_index('person').to_dict()['coefficient']
roles = {'writer':1, 'director':1, 'producer':1,'actor':1,'actress':1, 'self':1}


# snl_films = ['The Blues Brothers','Wayne's World','Coneheads','Wayne's World 2','It's Pat','Stuart Saves His Family','Blues Brothers 2000','A Night at the Roxbury','Superstar','The Ladies Man','MacGruber']
