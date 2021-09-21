# load the performers.csv

performers = pd.read_csv("actors.csv")
performers['coefficient'] = ''
writers = pd.read_csv("writers.csv")
writers['coefficient'] = ''

#SNL Coefficient calculations (ranked from most important value to least important value)

def get_coefficient(dataframe, row, column):
    person = dataframe["person"].values[row.name]
    if person != "Lorne Michaels":
        credit_type = dataframe["num_seasons"].values[row.name]
        num_seasons_writer = dataframe["num_seasons_writer"].values[row.name]
        num_seasons_headwriter = dataframe["num_seasons_headwriter"].values[row.name]
        num_seasons_actor = dataframe["num_seasons_actor"].values[row.name]
        num_seasons_rep	 = dataframe["num_seasons"].values[row.name]
        num_seasons_featured = dataframe["num_seasons_featured"].values[row.name]
        num_seasons_middle = dataframe["num_seasons_middle"].values[row.name]
        num_seasons_weekend_update = dataframe["num_seasons_weekend_update"].values[row.name]
        num_episodes_weekend_updates = dataframe["num_episodes_weekend_updates"].values[row.name]
        best_of = dataframe["best_of"].values[row.name] ##(this will be an either/or value)	
        num_episodes_headwriter = dataframe["num_episodes_headwriter"].values[row.name]	
        num_epsiodes_writer = dataframe["num_epsiodes_writer"].values[row.name]	
        num_episodes_actor = dataframe["num_episodes_actor"].values[row.name]
        num_episodes_hosted = dataframe["num_episodes_hosted"].values[row.name]											
        num_episodes_hosted/17 = host #(the highest number of times one has hosted)
        num_episodes_weekend_updates/num_episodes = F
        num_episodes_headwriter/num_episodes = I
        num_seasons/46 = A 
        num_seasons_rep/num_seasons = B 
        (num_seasons_featured + num_seasons_middle)/num_seasons = C 
        num_episodes/912 = H
        num_episodes_actor/num_episodes = K 
        num_epsiodes_writer/num_episodes = J
        coefficient = .1(host) + .1(best_of) + .1(E) + .1(F) + .1(I) + .25(.1(H)+.45(K)+.45(J)) + .25(.1(A)+.45(B)+.45(C))
        dataframe.at[row.name,column]= coefficient
    else:
        dataframe.at[row.name,column] = 1

performers.apply(lambda row: get_coefficient(performers, row, "coefficient"), axis=1)
writers.apply(lambda row: get_coefficient(writers, row, "coefficient"), axis=1)



		