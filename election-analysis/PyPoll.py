# Final Script:
    # Total number of votes cast
    # A complete list of candidates who received votes
    # Total number of votes each candidate received
    # Percentage of votes each candidate won
    # The winner of the election based on popular vote

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election-analysis.txt")

# total vote counter, create before with open()
total_votes = 0

# declare new list, create before with open()
candidate_options = []

# declare new dictionary, curly brackets, create before with open()
candidate_votes = {}

# declare empty string value for winning candidate
winning_candidate = ""

# set winning count to zero
winning_count = 0

# set winning percentage to zero
winning_percentage = 0

# Open the election results and read the file.
# Ensure for is within with open() to activate
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

# Print each row in the CSV file.
    for row in file_reader:
        # to print:
            # print(row)
        # Add to total votes, accumulator: "+= 1"
        total_votes += 1
        
        # print candidate name from each row
        candidate_name = row[2]

        # if candidate does not match any existing candidate
        if candidate_name not in candidate_options:

            # add candidate names to options list
            candidate_options.append(candidate_name)

            # tracking candidate's vote count, set to 0 ensure for loop resets
            candidate_votes[candidate_name] = 0

        # accumulator
        candidate_votes[candidate_name] += 1
    
    # save results to txt file
    with open(file_to_save, "w") as txt_file:

    # print the final vote count
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        
        # save the final vote count to the text file
        txt_file.write(election_results)

        # for loop to iterate through candidates
        for candidate_name in candidate_votes:

            # vote count
            votes = candidate_votes[candidate_name]

            # for percentages, one decimal
            vote_percentage = float(votes) / float(total_votes) * 100

            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            print(candidate_results)

            txt_file.write(candidate_results)

            # Determine winning vote count and candidate
            # Determine if the votes are greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):

                # If true then set winning_count = votes and winning_percent =
                winning_count = votes
                winning_percentage = vote_percentage

                # set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name

        winning_candidate_summary = (
                f"-------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"-------------------------\n")

        print(winning_candidate_summary)

        txt_file.write(winning_candidate_summary)