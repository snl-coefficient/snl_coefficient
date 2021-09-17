# load the performers.csv
person,
num_seasons, -- most important
repertory_player, -- second important
featured_player, -- less important
middle_group, -- less important (consider as featured_player)
weekend_update, -- important
hosted, -- important
best_of, -- important
writer, -- important
producer - 

person	
year_start	
year_end	

num_seasons_writer	
num_seasons_headwriter	
num_seasons_actor


SNL Coefficient calculations (ranked from most important value to least important value)

num_episodes_hosted/17 (the highest number of times one has hosted) = L (10%)
best_of = G (this will be an either/or value) (10%)

num_seasons_weekend_update/num_seasons = E (10%)
num_episodes_weekend_updates/num_episodes = F (10%)
num_episodes_headwriter/num_episodes = I  (10%)

(25%)
num_seasons/46 = A (10%)
num_seasons_rep/num_seasons = B (50%)
(num_seasons_featured + num_seasons_middle)/num_seasons = C (40%)

(25%)
num_episodes/912 = H 10%)
num_episodes_actor/num_episodes = K (45%) 
num_epsiodes_writer/num_episodes = J (45%)

coefficient = .1(L) + .1(G) + .1(E) + .1(F) + .1(I) + .25(.1(H)+.45(K)+.45(J)) + .25(.1(A)+.45(B)+.45(C))


		