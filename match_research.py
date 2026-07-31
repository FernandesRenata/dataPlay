from statsbombpy import sb

def target_matches(team_one, team_two, teams, matches):
    team_one = teams[17]
    team_two = teams[20]

    target_matches = matches[
        ((matches['home_team'] == team_one) & (matches['away_team'] == team_two)) |
        ((matches['home_team'] == team_two) & (matches['away_team'] == team_one))
    ]

    target_matches = target_matches['match_id'].tolist()

    return target_matches