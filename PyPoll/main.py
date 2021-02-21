import os

import csv
csvpath = os.path.join('election_data.csv')

total_votes = 0
candidates = {}
most_votes = 0
winner = ""

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)


    # Read each row of data after the header
    for row in csvreader:
        total_votes = total_votes +1
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        else:
            candidates[candidate_name] = candidates[candidate_name] +1
        

print("Election Results")
print("----------------------------")
print(f'Total Votes: {total_votes}')
print("----------------------------")
for candidate_name in candidates:
    print(f'{candidate_name}: {(candidates[candidate_name] / total_votes) * 100:.2f}% ({candidates[candidate_name]})')
    if candidates[candidate_name] > most_votes: 
              most_votes = candidates[candidate_name]
              winner = candidate_name
print("----------------------------")
print(f'Winner: {winner}')
print("----------------------------")

with open("election analysis.txt", "w") as textfile: 
    textfile.write("Election Results\n")
    textfile.write("----------------------------\n")
    