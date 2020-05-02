import csv
import os

# assign a variable for the file to load from the path
file_to_load = os.path.join('Resources','election_results.csv')
# assign a variable to save the file to a path
file_to_save = os.path.join('Analysis','election_analysis.txt')

# initialize a total vote counter
total_votes = 0

# candidate options & votes; county names & votes
county_list = []
county_votes = {}
candidate_options = []
candidate_votes = {}

# track the county with largest vote count; same for winning candidate (but include % contribution to election)
county_largest_turnout = ''
county_largest_turnout_count = 0
winning_candidate = ''
winning_count = 0
winning_percentage = 0

# open the election results and read the file
with open(file_to_load) as election_data:
        file_reader = csv.reader(election_data)

        # read and print the header row
        headers = next(file_reader)
        
        # print each row in the CSV file
        for row in file_reader:
                # add to the total vote count
                total_votes += 1

                # get county name & candidate name from each row
                county_name = row[1]
                candidate_name = row[2]

                # if the county doesn't match any existing county then add to county list
                if county_name not in county_list:
                        # add county to county list
                        county_list.append(county_name)

                        # start tracking that county's voter count
                        county_votes[county_name] = 0

                # add a vote to that county's count
                county_votes[county_name] += 1

                # if the candidate doesn't match any existing candidate then add to candidate list
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
                        f'--------------------------\n'
                        f'County Votes:\n')
                print(election_results, end='')
                # save the final vote count to the text file
                txt_file.write(election_results)
        
        # determine % of votes for each county by looping through the counts
        for county_name in county_list:
                # retrieve vote count & percentage
                c_votes = county_votes[county_name]
                c_vote_percentage = int(c_votes)/int(total_votes)*100

                county_results = (f'{county_name}: {c_vote_percentage:.1f}% ({c_votes:,})\n')
                # print each county, its vote count and  % of votes to the terminal    
                print(county_results)

                # save the county results to our text file
                txt_file = open('Analysis/election_analysis.txt', 'a')   
                txt_file.write(county_results)
                txt_file.close()

                # determine county with largest turnout
                if (c_votes > county_largest_turnout_count):
                        county_largest_turnout_count = c_votes
                        county_largest_turnout = county_name

        # print the name of the county with largest turnout to the terminal
        county_largest_turnout_summary = (
                f'---------------------------\n'
                f'Largest County Turnout: {county_largest_turnout}\n'
                f'---------------------------\n')
        print(county_largest_turnout_summary)
        # save county largest turnout summary to the text file
        txt_file = open('Analysis/election_analysis.txt', 'a')
        txt_file.write(county_largest_turnout_summary)
        txt_file.close()

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