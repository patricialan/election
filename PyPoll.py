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
candidate_votes = {}

# track the winning candidate, vote count, and percentage
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
                # add to the total vote count
                total_votes += 1

                # get candidate name from each row
                candidate_name = row[2]

                # if the candidate doesn't match any existing candidate
                # then add to candidate list
                if candidate_name not in candidate_options:
                        # add candidate name to candidate list
                        candidate_options.append(candidate_name)

                        # start tracking that candidate's voter count
                        candidate_votes[candidate_name] = 0

                # add a vote to that candidate's count
                candidate_votes[candidate_name] += 1

        # save the results to our text file
        with open(file_to_save, 'w') as txt_file:
        # print the final vote count to the terminal
                election_results = (
                        f'\nElection Results\n'
                        f'--------------------------\n'
                        f'Total Votes: {total_votes:,}\n'
                        f'--------------------------\n')
                print(election_results, end='')
                # save the final vote count to the text file
                txt_file.write(election_results)
        
        # determine % of votes for each candidate by looping through the counts
        for candidate_name in candidate_options:
                # retrieve vote count & percentage
                votes = candidate_votes[candidate_name]
                vote_percentage = int(votes)/int(total_votes)*100

                candidate_results = (f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
                # print each candidate, their vote count and  % of votes to the terminal
                print(candidate_results)

                # save the candidate results to our text file
                txt_file = open('Analysis/election_analysis.txt', 'a')   
                txt_file.write(candidate_results)
                txt_file.close()

                # determine winning vote count, winning percentage, and candidate
                if (votes > winning_count) and (vote_percentage > winning_percentage):
                        winning_count = votes
                        winning_percentage = vote_percentage
                        winning_candidate = candidate_name

        # print the winning candidate's results to the terminal
        winning_candidate_summary = (
                f'---------------------------\n'
                f'Winner: {winning_candidate}\n'
                f'Winning Vote Count: {winning_count:,}\n'
                f'Winning Percentage: {winning_percentage:.1f}%\n'
                f'---------------------------\n')
        print(winning_candidate_summary)
        # save winning candidate's summary to the text file
        txt_file = open('Analysis/election_analysis.txt', 'a')
        txt_file.write(winning_candidate_summary)
        txt_file.close()