# get a list of media types from making a set of of all the values in all the lists in that column 
# and then see what media types you get 
# and then move the media type over to a new "media_type" column 
list_of_info = dataframe[column].values[row.name]
media_types = []
for media in media_types:
    if media in list_of_info: 
        media_type = media 
    else:
        media_type = "Film"
        
if string contains dates: #(whatever i do to get years from another script):
    start_year = 
    end_year = 


for item in list_of_info:
    item = item.strip()
    non_number = re.compile(r'[^\d]+')
    new_item = non_number.sub('',item)
    new_item = re.sub('[()]', '', new_item)
    revised_list.append(new_item)
    revised_list = [x.strip() for x in revised_list if x.strip()]
    revised_list = [i for i in revised_list if i]
    only_numbers = []
    for item in revised_list:
        split_strings = [item[index : index + 4] for index in range(0, len(item), n)]
        for item in split_strings:
            if len(item) == 4:
                item = int(item)
                only_numbers.append(item)
      if len(only_numbers) != 0:
          dataframe.at[row.name,'year_start'] = str(min(only_numbers))
          dataframe.at[row.name,'year_end'] = str(max(only_numbers))

#[word for line in mylist for word in line.split()]