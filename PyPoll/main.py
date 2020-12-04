import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')

# total number of votes

total_votes = 0
list_candidates =[]
list_votes =[]
#candidates_dict = candidate
with open(election_csv) as csv_file:
    #csv_reader = csv.reader(csv_file, delimiter=",")
    csv_reader_object = csv.reader(csv_file)
    if csv.Sniffer().has_header:
        next(csv_reader_object)
    for row in csv_reader_object:
        total_votes +=1
        #candidates_dict[
        if (row[2] not in list_candidates):
            list_candidates.append(row[2])
           

    

str_total_votes = str(total_votes)
print("Total Votes : " +str_total_votes)
print(list_candidates)


    
