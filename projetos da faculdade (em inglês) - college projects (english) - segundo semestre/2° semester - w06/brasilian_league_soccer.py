import csv

TEAM_NAME_INDEX = 0
TEAM_MACTHES_INDEX = 1
TEAM_WINS_INDEX = 2
TEAM_DRAW_INDEX = 3
TEAM_DEFEAT_INDEX = 4

def main():

    team_list = teams_dictionary_file() # store the dictionary in a variable
    
    total_scores = 0 #Viariable that will sum the total score
    count = 1   # variable that will count the teams
    # print team list

    print(f"Power Rankings:\n")

    #for inner in team_list:
    for key, value in team_list.items(): # separate the list value and key value

        #   The teams score 3 points for each win, 1 point for each draw
        #   and no point in case of defeat. 
        team_name = value[0]

        if team_name == key:    
                    
            team_wins = value[2]
            team_draw = value[3]

            total_scores = (int(team_wins) * 3) + int(team_draw)    # calculating the total scores of each team
            print( team_list)
            #add the total scores into each team dictionary
            team_list[key] = total_scores
            
            try:    #   creating an excpition
                ranking = dict(sorted(team_list.items(), # ranking teams in scoring order 
                    key=lambda item: item[1], reverse=True))
                
                for key, value in ranking.items():
                    if count == 1:
                        print(f"{key}: With {value} points. Is the winner of Brasilian 2023 League Soccer!\n")
                        print(f"The teams below are qualified for 2024 regional Cups.\n")
                    elif count <= 4:
                        print(f"{key} is qualified for 2024 Libertadores Cup with {value} points.")
                    elif count == 5:
                        print(f"{key} is qualified for 2024 Sudamericana Cup with {value} points.\n")
                        print(f"The teams below will not play any regional cup in 2024.\n")
                    else:    
                        print(f"{key}: {value} points.")    # print the team and its total score                 

                    count += 1  # count the next team in score order

            except TypeError as type_err:
                print
                
                
 
def teams_dictionary_file():

    teams_dict= {}  # create a dictionary

    with open("2° semester - w06/brasilian_teams_raking.csv") as teams_file:
        
        reader = csv.reader(teams_file) #The reader object returns each row as a list.

        next(reader)    # skip the first line

        #   
        for teams in reader:
            key = teams[0]
            teams_dict[key] = teams

    return teams_dict


if __name__ == "__main__":
    main()