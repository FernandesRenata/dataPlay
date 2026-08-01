from statsbombpy import sb

from match_statistics import match_summary
from match_selection import match_selection
from match_research import target_matches
from heatmap import team_heatmap
from player_events import calculate_player_statistics

import pandas as pd

matches = sb.matches(
    competition_id=72,
    season_id=107
)

team_one, team_two, teams = match_selection(matches)

match_ids = target_matches(team_one=team_one, team_two=team_two, teams=teams, matches=matches)

all_events = []

for match_id in matches["match_id"]:

    events = sb.events(match_id=match_id)
    events["match_id"] = match_id

    all_events.append(events)

events = pd.concat(all_events, ignore_index=True)

player_statistics = calculate_player_statistics(events)

print("Choose the match you want to analyze:\n")

for i, match_id in enumerate(match_ids):
    partida = matches[matches["match_id"] == match_id].iloc[0]

    print(
        f"{i} - {partida['match_date']} | "
        f"{partida['home_team']} x {partida['away_team']}"
    )
target_id = int(input("\nChoose the match:\n"))
target_id = match_ids[target_id]

print(match_summary(target_id))


player_statistics.to_csv(
    "player_statistics.csv",
    index=False,
    encoding="utf-8-sig"
)