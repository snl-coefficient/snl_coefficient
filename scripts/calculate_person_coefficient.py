# load the performers.csv
import pandas as pd 
import csv 

performers = pd.read_csv("actors_with_snl_credits.csv")
performers.fillna(0, inplace=True)
performers['num_episodes_other'] = ''
performers['coefficient'] = ''
snl_credits = pd.read_csv("only_snl_filmography.csv")
snl_credits.fillna(0, inplace=True)

def get_coefficient(dataframe, row, column):
    person = dataframe["person"].values[row.name]
    print(person)
    person_dataframe = snl_credits[snl_credits["person"]==person]
    num_episode_counts = person_dataframe["total_episode_count"].to_list()
    num_episodes = sum(num_episode_counts)
    roles_to_exclude = ['actor', 'writer','actress']
    credit_dataframe = person_dataframe[~person_dataframe['credit_type'].isin(roles_to_exclude)] 
    if credit_dataframe.shape[0] != 0:
        other_episode_counts = credit_dataframe["total_episode_count"].to_list()
        other = sum(other_episode_counts)
        performers.at[row.name,'num_episodes_other'] = other
        other = other/913
        other = .1 * other
    else:
        other = 0
        performers.at[row.name,'num_episodes_other'] = other
    num_seasons = int(dataframe["num_seasons_total"].values[row.name])
    #num_episodes_total = int(dataframe["num_episodes_total"].values[row.name])
    num_seasons_writer = int(dataframe["num_seasons_writer"].values[row.name])
    num_seasons_headwriter = int(dataframe["num_seasons_headwriter"].values[row.name])
    num_seasons_actor = int(dataframe["num_seasons_actor"].values[row.name])	
    num_seasons_rep	 = int(dataframe["num_seasons_rep"].values[row.name])	
    num_seasons_featured = int(dataframe["num_seasons_featured"].values[row.name])	
    num_seasons_middle = int(dataframe["num_seasons_middle"].values[row.name])	
    num_seasons_weekend_update = int(dataframe["num_seasons_weekend_update"].values[row.name])	
    num_episodes_weekend_update = int(dataframe["num_episodes_weekend_updates"].values[row.name])	
    best_of = int(dataframe["best_of"].values[row.name])	 ##(this will be an either/or value)
    best_of = int(.1 * best_of) 	
    #num_episodes_headwriter = int(dataframe["num_episodes_headwriter"].values[row.name])	
    num_episodes_writer = int(dataframe["num_episodes_writer"].values[row.name])	
    num_episodes_actor = int(dataframe["num_episodes_actor"].values[row.name])
    num_episodes_hosted = int(dataframe["num_episodes_hosted"].values[row.name])											
    host = num_episodes_hosted/17 #(the highest number of times one has hosted)
    host = int(.1 * host)
    try:  
        A = num_seasons/47 
        B = num_seasons_rep/num_seasons 
        C = (num_seasons_featured + num_seasons_middle)/num_seasons
        E = num_seasons_weekend_update/num_seasons
        F = num_episodes_weekend_update/913#num_episodes
        I = num_seasons_headwriter/num_seasons
        J = num_episodes_writer/913
        K = num_episodes_actor/913
        host_coefficient = int(host + best_of)
        coefficient = host_coefficient + (.15*F) + (.15*I) + .25*(other + (.46*K)+(.44*J)) + .25*((.2*A)+(.36* B)+(.34*C)) #+ (.1*E)
        #print(person, num_seasons, coefficient, A, B, C, E, F, I, J, K)
        dataframe.at[row.name,column] = coefficient
    except: 
        print(person, "problem")
        dataframe.at[row.name,column] = 0
    #else:
        #dataframe.at[row.name,column] = 1
    if person == "Lorne Michaels":
        dataframe.at[row.name,column] = 1
performers.apply(lambda row: get_coefficient(performers, row, "coefficient"), axis=1)
performers.to_csv("performers_with_coefficient.csv", index=False)



		