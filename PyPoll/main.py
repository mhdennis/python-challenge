#Import dependencies 
import os
import csv
import pandas as pd 

#Bring in CSV file
election_data = os.path.join("election_data_1.csv")
csv_path = "raw_data/election_data_1.csv"

#Create dataframe
pd.read_csv(csv_path)
election_df = pd.read_csv(csv_path)

#Find total votes
total_votes = election_df["Voter ID"].count()

#Find unique candidates
candidate = election_df["Candidate"].unique()

#Find winning candidate
max_candidate = election_df["Candidate"].max()

#Find value count for each candidate
candidate_votes = election_df["Candidate"].value_counts()

#Find percentage of total votes won for each candidate
percentage_won = ((candidate_votes/total_votes)*100)
final_percentages = percentage_won.map("{0:,.1f}%".format)

#Print Results

print("Election Results")
print("----------------------")
print("Total Votes: " + str(total_votes))
print("----------------------")
print(candidate[0] + ":" + " " + str(final_percentages[0]) + "(" + str(candidate_votes[0]) + ")") 
print(candidate[1] + ":" + " " + str(final_percentages[1]) + "(" + str(candidate_votes[1]) + ")")
print(candidate[2] + ":" + " " + str(final_percentages[2]) + "(" + str(candidate_votes[2]) + ")")
print(candidate[3] + ":" + " " + str(final_percentages[3]) + "(" + str(candidate_votes[3]) + ")")
print("----------------------")
print("Winner: " + str(max_candidate))
print("----------------------")


#Output to txt file 
#in terminal use:
#python main.py > pypoll.txt 

import subprocess
with open("pypoll.txt", "w+") as output:
    subprocess.call(["python", "./main.py"], stdout=output);



