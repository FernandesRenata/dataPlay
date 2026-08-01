from statsbombpy import sb

def team_selection(matches):

    print("Choose a team to analyze: \n")

    home_team = matches["home_team"].tolist()
    away_team = matches["away_team"].tolist()

    teams = home_team + away_team

    teams = sorted(list(set(teams)))

    for i in range(len(teams)):
        print(f"{i} - {teams[i]}")


    team = int(input("\nChoose the number:\n"))
   
    team = teams[team]

    return(team)