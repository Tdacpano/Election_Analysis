#Add our dependencies
import csv
import os
#Assign a variable for the file to load annd the path
file_to_load = 'Resources/election_results.csv'
#Create a filename variable for the file to load annd the path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

#Print the candidate name from each row
candidate_options = []

#Create a candidate dictionary
candidate_votes = {}

#Declare a variable that holds an empty string value for winning candidate
winninng_candidate = " "
#Declare a vairable for the "winning_count" equal to 0
winning_count = 0
#Declare a vairable for the "winning_percentage " equal to 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

        #To do: Read and Analyze the data here

# Print the header row.
    headers = next(file_reader)
    
#Print eachh row in the CSV file
    for row in file_reader:
   # 2.Increment the toal votes by 1
        total_votes += 1

    #Print the Candidates names 
        candidate_name = row[2]

#If candidate does not match any exisiting candidate.. 
        if candidate_name not in candidate_options:
    
     # Add the candidate name to the candidate list.
           candidate_options.append(candidate_name)
    
    #dictionary for the candidate and votes
           candidate_votes[candidate_name] = 0
    #add a vote to each count
        candidate_votes[candidate_name] += 1


# Determine teh percentage of votes for each candidate
    #. Iterate through the candidate list
for candidate_name in candidate_votes:
    #. Retrieve vote counnt of a candidate.
    votes = candidate_votes[candidate_name]
    #.Calculate the percentage of the vote count
    vote_percentage = float(votes) / float(total_votes)*100
   #  To do: print out the winning candidate, vote count and percentage to terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
       #. If true then set winning_count = votes and winning_percent = vote_percentage.        
            winning_percentage = votes 
            winning_percentage = vote_percentage
        #. Set the winning_candidate equal to the candidate's name.
            winninng_candidate = candidate_name
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winninng_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)      







  



   