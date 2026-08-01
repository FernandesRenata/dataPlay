from statsbombpy import sb
import pandas as pd

from team_selection import team_selection
from player_events import calculate_player_statistics
from player_by_game_time import calculate_minutes
from feature_engineering import create_features

COMPETITION_ID = 72
SEASON_ID = 107

matches = sb.matches(
    competition_id=COMPETITION_ID,
    season_id=SEASON_ID
)

team = team_selection(matches)

season_statistics = []

for match_id in matches["match_id"]:

    events = sb.events(match_id=match_id)

    events = events[
        events["team"] == team
    ]

    if events.empty:
        continue

    stats = calculate_player_statistics(events)

    minutes = calculate_minutes(events)

    stats = stats.merge(
        minutes,
        on="player",
        how="left"
    )

    season_statistics.append(stats)


season_statistics = pd.concat(
    season_statistics,
    ignore_index=True
)

numeric_columns = [
    "passes",
    "completed_passes",
    "progressive_passes",
    "key_passes",
    "assists",
    "shots",
    "goals",
    "xG",
    "xA",
    "dribbles",
    "recoveries",
    "interceptions",
    "pressures",
    "tackles",
    "minutes"
]

season_statistics = (
    season_statistics
    .groupby(
        ["player", "team"],
        as_index=False
    )[numeric_columns]
    .sum()
)

season_statistics = season_statistics[
    season_statistics["minutes"] > 0
]

metrics = [
    "passes",
    "completed_passes",
    "progressive_passes",
    "key_passes",
    "assists",
    "shots",
    "goals",
    "xG",
    "xA",
    "dribbles",
    "recoveries",
    "interceptions",
    "pressures",
    "tackles"
]

for metric in metrics:

    season_statistics[f"{metric}_p90"] = (
        season_statistics[metric] /
        season_statistics["minutes"]
    ) * 90

season_statistics = create_features(
    season_statistics
)

season_statistics.to_csv(
    "team_statistics.csv",
    index=False,
    encoding="utf-8-sig"
)

print(season_statistics.head())