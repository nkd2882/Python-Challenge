# PyPoll Challenge - Election Analysis Script
 
# Import necessary modules
import os
import csv
from collections import Counter
 
# Define paths for input and output files
election_csv = os.path.join("/Users/nkd/Documents/Data_Science_Class/Starter_Code-4/PyPoll/Resources", "election_data.csv")
output_file = os.path.join(os.path.dirname(__file__), "Analysis", "election_analysis.txt")
 
# Initialize a Counter to store candidate votes
candidates = Counter()
 
# Initialize total vote count
total_votes = 0
 
# Read and process the CSV file
with open(election_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
 
    # Skip the header row
    next(csv_reader)
 
    # Iterate through each row in the CSV
    for row in csv_reader:
        # Count total votes
        total_votes += 1
 
        # Count votes for each candidate
        candidate = row[2]
        candidates[candidate] += 1
 
# Calculate results
results = []
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, percentage, votes))
 
# Sort results by number of votes in descending order
results.sort(key=lambda x: x[2], reverse=True)
 
# Determine the winner
winner = results[0][0]
 
# Prepare the analysis results
analysis_results = f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""
 
for candidate, percentage, votes in results:
    analysis_results += f"{candidate}: {percentage:.3f}% ({votes})\n"
 
analysis_results += f"""-------------------------
Winner: {winner}
-------------------------
"""
 
# Print results to terminal
print(analysis_results)
 
# Write results to output file
with open(output_file, "w") as file:
    file.write(analysis_results)
 
print(f"Analysis has been saved to {output_file}")