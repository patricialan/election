import csv
import os

# assign a variable for the file to load from the path
file_to_load = os.path.join('Resources','election_results.csv')

# assign a variable to save the file to a path
file_to_save = os.path.join('Analysis','election_analysis.txt')

# open the election results and read the file
with open(file_to_load) as election_data:

        # read the file object with the reader function
        file_reader = csv.reader(election_data)

        # read and print the header row
        headers = next(file_reader)
        print(headers)
        
        # print each row in the CSV file
        for row in file_reader:
                print(row)

# using with statement, open the file as a text file
with open(file_to_save, 'w') as txt_file:

    # write 3 counties to the file
    txt_file.write('Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson')