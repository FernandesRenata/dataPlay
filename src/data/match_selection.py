from statsbombpy import sb

def match_selection(matches):

    print("Let's analyze Women's World Cup\n\n")

    home_team = matches["home_team"].tolist()
    away_team = matches["away_team"].tolist()

    teams = home_team + away_team

    teams = sorted(list(set(teams)))

    for i in range(len(teams)):
        print(f"{i} - {teams[i]}")

    team_one = ''
    team_two = ''

    
    team_one = int(input("\nChoose the first team:\n"))
    team_two = int(input("\nChoose the second team:\n"))

    team_one = teams[team_one]
    team_two = teams[team_two]

    return(team_one, team_two, teams)