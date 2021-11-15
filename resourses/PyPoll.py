# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.



# Assign a variable for the file to load and the path
# file_to_load = 'Resourses/election_results.csv'
# Open the election results and read the file.
# with open(file_to_load) as election_data:

    # To do: perform analysis.
#    print(election_data)

# Close the file.
# election_data.close()

# Add our dependancies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("resourses", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: read and analyze the data here
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)




# Using the with statementopen the file as a text file.
# with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    # txt_file.write("Counties in the Election\n------------------\nArapahoe\nDenver\nJefferson")
