import csv
import os

# assign a variable for the file to load from the path
file_to_load = os.path.join('Resources','election_results.csv')
# assign a variable to save the file to a path
file_to_save = os.path.join('Analysis','election_analysis.txt')

# initialize a total vote counter
total_votes = 0

# candidate options and candidate votes
candidate_options = []
# declare an empty dictionary
candidate_votes = {}

# winning candidate and winning count tracker
winning_candidate = ''
winning_count = 0
winning_percentage = 0

# open the election results and read the file
with open(file_to_load) as election_data:
        file_reader = csv.reader(election_data)

        # read and print the header row
        headers = next(file_reader)
        print(headers)
        
        # print each row in the CSV file
        for row in file_reader:
                # add each vote to total_votes
                total_votes += 1

                # print candidate name from each row
                candidate_name = row[2]

                if candidate_name not in candidate_options:
                        # add candidate name to candidate list
                        candidate_options.append(candidate_name)

                        # start tracking that candidate's vote count
                        candidate_votes[candidate_name] = 0

                # add a vote to that candidate's count
                candidate_votes[candidate_name] += 1
        
        # determine % of votes for each candidate by looping through the counts
        # 1. iterate through candidate list
        for candidate_name in candidate_options:
                # 2. get vote count of each candidate
                votes = candidate_votes[candidate_name]

                # 3. calculate % of votes
                vote_percentage = int(votes)/int(total_votes)*100

                # TO DO: 4. print candidate name, vote count, and % of votes
                print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')

                # determine winning vote count and candidate
                # A. determine if the votes are greater than the winnng count
                if (votes > winning_count) and (vote_percentage > winning_percentage):
                        # B. if true then set winning_count = votes and winning_percent = vote_percentage
                        winning_count = votes
                        winning_percentage = vote_percentage
                        # C. Set the winning_candidate equal to the candidate's name
                        winning_candidate = candidate_name

        # TO DO: print the winning candidate, vote count, and %
        winning_candidate_summary = (
                f'---------------------------\n'
                f'Winner: {winning_candidate}\n'
                f'Winning Vote Count: {winning_count:,}\n'
                f'Winning Percentage: {winning_percentage:.1f}%\n'
                f'---------------------------\n')
        print(winning_candidate_summary)

# using with statement, open the file as a text file
with open(file_to_save, 'w') as txt_file:

    # write 3 counties to the file
    txt_file.write('Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson')