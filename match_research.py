from statsbombpy import sb

matches = sb.matches(
    competition_id=43,
    season_id=106
)

home_team = matches["home_team"].tolist()
away_team = matches["away_team"].tolist()

teams = home_team + away_team

teams = list(set(teams))

for i in range(len(teams)):
    print(f"{i} - {teams[i]}")

team_one = teams[14]
team_two = teams[0]

team_one_matches = matches[(matches['home_team'] == team_one) | (matches['away_team'] == team_one)]
target_matches = team_one_matches[(matches['home_team'] == team_two) | (matches['away_team'] == team_two)]

print(target_matches)