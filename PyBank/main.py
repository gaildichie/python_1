import os
import csv

# Path to the CSV file
election_csv = os.path.join("../Resources/ election_data.csv")

# Initialize variables
total_votes = 0
candidates = {}
winner_votes = 0
winner_name = ""

# Read the CSV file
with open(election_csv, 'r') as file:
    csv_reader = csv.reader(file)
    
    # Skip the header
    next(csv_reader)
    
    # Iterate through each row in the CSV
    for row in csv_reader:
        total_votes += 1
        candidate_name = row[2]
        
        # Count votes for each candidate
        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        else:
            candidates[candidate_name] += 1

# Print Election Results
print("Election Results")
print("---------------------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------------------")

# Calculate and print the percentage of votes for each candidate
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage}% ({votes})")
    
    # Determine the winner
    if votes > winner_votes:
        winner_votes = votes
        winner_name = candidate

print("---------------------------------------")
print(f"Winner: {winner_name}")
print("---------------------------------------")

    