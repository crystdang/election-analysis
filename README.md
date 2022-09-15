# Module 3 Challenge Analysis: Election Audit
## by Crystina Dang using Python v3.9.12




## Overview of Election Audit:

The election commissioner requested the following information for use in an election audit:
		
1. The voter turnout for each county
2. The percentage of votes from each county out of the total count
3. The county with the highest turnout

The purpose of this analysis is to present the results extracted from the provided data set and how they were established.

## Election Audit Results:

The following results were established using [this dataset](Resources/election_results.csv) and [this code](PyPoll_Challenge.py):

  - Total Votes: *369,711*

##### Code used:
```    
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

```
The data set provided was of each ballot, or also referred to as votes, and by counting each row and skipping the header, the total votes could be established.



```		
		# For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the county does not match any existing county in the county list.
        if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1
```
By adding multiple accumulators (x = x + 1 OR x += 1) within a for loop for categorizing each ballot by candidate and county, the data is organized while also storing seperate total counts.



  - County Votes:
      - **Jefferson:** *10.5% (38,855)*
      - **Denver:** *82.8% (306,055)*
      - **Arapahoe:** *6.7% (24,801)*

```
  for county_name in county_votes:

        # 6b: Retrieve the county vote count.
        turnout = county_votes.get(county_name)

        # 6c: Calculate the percentage of votes for the county.
        county_percentage = float(turnout) / float(total_votes) * 100
        turnout_results = (f"{county_name}: {county_percentage:.1f}% ({turnout:,})\n")
```
The county votes were organized in the previous code and percentages could be easily calculated by dividing each total to the total votes.

  - Largest County Turnout: **Denver**
```
       # 6f: Write an if statement to determine the winning county and get its vote count.
        if (turnout > largest_turnout_count) and (county_percentage > largest_turnout_percentage):
            largest_turnout_count = turnout
            largest_turnout = county_name
            largest_turnout_percentage = county_percentage
```
The largest turnout can easily be proven by using an if statement

  - Candidate Votes:
      - **Charles Casper Stockham:** *23.0% (85,213)*
      - **Diana DeGette:** *73.8% (272,892)*
      - **Raymon Anthony Doane:** *3.1% (11,606)*

  - Winner: 
      - **Winning Candidate:** *Diana DeGette*
      - **Winning Vote Count:** *272,892*
      - **Winning Percentage:** *73.8%*

  [This text file](analysis/election_results.txt) was created reflecting this results as well.


## Election Audit Summary: 
In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.

There is a statement to the election commission that explores how this script can be used for any election, with two examples for modifying the script. (4 pt)}
--
## Resources:
## Challenge Overview:
## Challenge Summary:

