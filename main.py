import csv
from collections import Counter

#Set the file path
file_path = "election_data.csv"

#Initialize variables
total_votes = 0
candidates = []

#Read the csv file and iterate over rows
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip the header row
    next(csvreader)
    for row in csvreader:
    #Increment the vote count
        total_votes += 1
    #Add the candidate to the list of candidates
    candidates.append(row[2])
    
#Count the number of votes for each candidate
vote_count = Counter(candidates)

#Calculate the percentage of votes for each candidate
percentages = {}
for candidate, count in vote_count.items():
    percentage = round((count / total_votes) * 100,3)
    percentages[candidate] = percentage
    
#Find the winner based on popular vote
winner = max(vote_count, key=vote_count.get)

#Print the analysis results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
for candidate, count in vote_count.items():
    print(f"{candidate}: {percentages[candidate]}% ({count})")
print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")

