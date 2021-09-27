# load the performers.csv
import pandas as pd 
import csv 

performers = pd.read_csv("snl_alums.csv")
performers['coefficient'] = ''

def get_coefficient(dataframe, row, column):
    person = dataframe["person"].values[row.name]
    print(person)
    if person != "Lorne Michaels":
        #num_seasons = int(dataframe["num_seasons_total"].values[row.name])
        #num_episodes_total = int(dataframe["num_episodes_total"].values[row.name])
        num_seasons_writer = int(dataframe["num_seasons_writer"].values[row.name])
        num_seasons_headwriter = int(dataframe["num_seasons_headwriter"].values[row.name])
        num_seasons_actor = int(dataframe["num_seasons_actor"].values[row.name])	
        num_seasons_rep	 = int(dataframe["num_seasons_rep"].values[row.name])	
        num_seasons_featured = int(dataframe["num_seasons_featured"].values[row.name])	
        num_seasons_middle = int(dataframe["num_seasons_middle"].values[row.name])	
        num_seasons_weekend_update = int(dataframe["num_seasons_weekend_update"].values[row.name])	
        num_episodes_weekend_updates = int(dataframe["num_episodes_weekend_updates"].values[row.name])	
        best_of = int(dataframe["best_of"].values[row.name])	 ##(this will be an either/or value)	
        num_episodes_headwriter = int(dataframe["num_episodes_headwriter"].values[row.name]	)	
        num_epsiodes_writer = int(dataframe["num_epsiodes_writer"].values[row.name])	
        num_episodes_actor = int(dataframe["num_episodes_actor"].values[row.name])
        num_episodes_hosted = int(dataframe["num_episodes_hosted"].values[row.name])											
        host = int(num_episodes_hosted/17) #(the highest number of times one has hosted)
        #A = int(num_seasons/46)
        # this is actually not right but we'll work with it for now 
        A = int(10/46)
        B = int(num_seasons_rep/A) 
        C = int((num_seasons_featured + num_seasons_middle)/A) 
        E = ??
        F = int(num_episodes_weekend_updates/num_episodes)
        I = int(num_episodes_headwriter/num_episodes)
        H = int(num_episodes/912)
        J = int(num_epsiodes_writer/num_episodes)
        K = int(num_episodes_actor/num_episodes) 
        coefficient = .1(host) + .1(best_of) + .1(E) + .1(F) + .1(I) + .25(.1(H)+.45(K)+.45(J)) + .25(.1(A)+.45(B)+.45(C))
        dataframe.at[row.name,column]= coefficient
    else:
        dataframe.at[row.name,column] = 1

performers.apply(lambda row: get_coefficient(performers, row, "coefficient"), axis=1)
#writers.apply(lambda row: get_coefficient(writers, row, "coefficient"), axis=1)



		