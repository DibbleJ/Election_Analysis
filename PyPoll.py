# Add our dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Create a filename variable to direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter
total_votes = 0
#candidate_options and candidate_votes
candidate_options = []
candidate_votes = {}
#Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winnng_count = 0
winning_percentage = 0
#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Read the header row.
    headers = next(file_reader)
    #Print each row in the csv file.
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1
        #Get the candidate name for each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0   
        #Add a vote to candidate vote count
        candidate_votes[candidate_name] += 1

#Save the results to text file.
with open(file_to_save,"w") as txt_file:
    election_results =(f"\nElection Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------\n")
    print(election_results,end="")
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # 4. Print the candidate name and percentage of votes.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        #Check for lead
        if (votes > winnng_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        
    #print(f"{winning_candidate} won the election with {winning_count} votes ({winning_percentage:.1f}%).")

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)