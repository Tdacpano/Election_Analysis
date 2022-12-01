#Add our dependencies
import csv
import os
#Assign a variable for the file to load annd the path
file_to_load = 'Resources/election_results.csv'
#Create a filename variable for the file to load annd the path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

        #To do: Read and Analyze the data here

# Print the header row.
    headers = next(file_reader)
    print(headers)

   