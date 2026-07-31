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

    print("\nChoose the first team:\n")
    input(team_one)

    print("\nChoose the second team:\n")
    input(team_two)


    return(team_one, team_two, teams)