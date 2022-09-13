
#list
counties = ["Arapahoe","Denver","Jefferson"]
counties
#defined list starts at 0
counties[0]
#select by index
print(counties[2])
#negative index starts from last at 1
print(counties[-1])
#count items
len(counties)
#slicing
counties[:2]
#add at edd
counties.append("El Paso")
counties
#add at specific index
counties.insert(2, "El Paso")
#remove by name, if duplicate, first will be removed
counties.remove("El Paso")
#search index number
i = counties.index("EL Paso")
counties[i] = "El Paso"
counties
#remove by index and will be named
counties.pop(3)
#replace by index
counties[2] = "El Paso"
#tuples are immutable
counties_tuple = ("Arapahoe","Denver","Jefferson")
#dictionaries have key and value
counties_dict= dict()
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict.items()
counties_dict.keys()
counties_dict.values()
counties_dict.get("Denver")
counties_dict['Arapahoe']
voting_data= []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data.insert(1, {"country":"El Paso", "registered_voters": 461149})
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
voting_data.remove({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
voting_data
# How many votes did you get?
# int() to confirm integer, str() to confirm string, input to ask question
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
# >= greater than or equal, == equal to (double when not formula), != not equal to
temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")
# indents are important in Python
#What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')
                #nested if-else statements: else if can be compounded to 'elif'
# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')
# readability will determine if-else or if-elif-else statement.

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
    # membership operators: 'in'/'not in'
# logical operators: 'and'/'or'/'not'
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")

# while loop == condition-controlled loop
# for look == count-controlled loop

x = 0
while x <= 5:
    print(x)
    x = x + 1
# produce following numbers

counties_tuple = ("Arapahoe","Denver","Jefferson")

for i in range(len(counties_tuple)):
      print(counties_tuple[i])
# create an index and use a range count to print lists

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
# for values only
for county in counties_dict:
    print(counties_dict[county])
for county in counties_dict:
    print(counties_dict.get(county))

#for both key and value
for county, voters in counties_dict.items():
    print(county, voters)

# SOLVED: Create text for Arapahoe county has 422829 registered voters.
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
# OR
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
      print(voting_data[i]['county'])
# key and value underneath
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
# just values
for county_dict in voting_data:
     print(county_dict['registered_voters'])
# just key
for county_dict in voting_data:
    print(county_dict['county'])

# without f-string - all must be turned into a string
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")
# use of f-string to simplify and automate integers into strings, f and curly brackets
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)
# decimals = f'{value:{width},.{precision}}'

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# UNSOLVED: output "Arapahoe county has 422,829 registered voters"
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:{0,000},0f} registered voters.")


# final script will have:
#Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote