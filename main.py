from statsbombpy import sb
from player_events import calculate_player_statistics
from team_selection import team_selection
import pandas as pd

all_events = []

matches = sb.matches(competition_id=72, season_id=107)

team = team_selection(matches)

for match_id in matches["match_id"]:

    events = sb.events(match_id=match_id)

    events = events[
        events["team"] == team
    ]

    events["match_id"] = match_id

    all_events.append(events)

events = pd.concat(all_events, ignore_index=True)

team_statistics = calculate_player_statistics(events)

team_statistics.to_csv(
    "team_statistics.csv",
    index=False,
    encoding="utf-8-sig"
)