from statsbombpy import sb
import pandas as pd
import warnings
from statsbombpy.api_client import NoAuthWarning

import src.data.team_selection
import src.features.player_events
import src.features.player_by_game_time
import src.features.feature_engineering
import src.visualization.charts

warnings.filterwarnings("ignore", category=NoAuthWarning)

COMPETITION_ID = 72
SEASON_ID = 107

matches = sb.matches(
    competition_id=COMPETITION_ID,
    season_id=SEASON_ID
)
player = input("Choose a player to analyze:\n")
player_statistics = []


team = src.data.team_selection.team_selection(matches)

print("...loading data for team:", team)

season_statistics = []

for match_id in matches["match_id"]:

    events = sb.events(match_id=match_id)

    events = events[
        events["team"] == team
    ]

    if events.empty:
        continue

    stats = src.features.player_events.calculate_players_statistics(events)

    minutes = src.features.player_by_game_time.calculate_minutes(events)

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
    "passes",   #mid-field
    "completed_passes", #mid-field
    "progressive_passes",   #mid-field
    "key_passes",   #mid-field
    "assists",  #attacking
    "shots",    #attacking
    "goals",    #attacking
    "xG",
    "xA",
    "dribbles",
    "recoveries",   #defensive
    "interceptions",    #defensive
    "pressures",    #defensive
    "tackles",  #defensive
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

season_statistics = src.features.feature_engineering.create_features(
    season_statistics
)

if player.strip():
    player_df = season_statistics[
        season_statistics["player"].str.contains(player.strip(), case=False, na=False)
    ]
    if not player_df.empty:
        player_statistics = player_df
    else:
        print(f"Player '{player}' not found. Analyzing all team players for charts.")
        player_statistics = season_statistics
else:
    player_statistics = season_statistics

player_statistics.to_csv(
    "player_statistics.csv",
    index=False,
    encoding="utf-8-sig"
)

season_statistics.to_csv(
    "team_statistics.csv",
    index=False,
    encoding="utf-8-sig"
)

top3_defenders = (
    season_statistics
    .sort_values(
        by="defensive_actions",
        ascending=False
    )
    .head(3)
)

top3_attackers = (
    season_statistics
    .sort_values(
        by="offensive_contribution",
        ascending=False
    )
    .head(3)
)

top3_midfielders = (
    season_statistics
    .sort_values(
        by="midfield_contribution",
        ascending=False
    )
    .head(3)
)

top3_attackers.to_csv(
    "top3_attackers.csv",
    index=False,
    encoding="utf-8-sig"
)

top3_defenders.to_csv(
    "top3_defenders.csv",
    index=False,
    encoding="utf-8-sig"
)

top3_midfielders.to_csv(
    "top3_midfielders.csv",
    index=False,
    encoding="utf-8-sig"
)

src.visualization.charts.goals_xg_p90_barplot(player_statistics)
src.visualization.charts.pressures_and_tackles_p90_barplot(player_statistics)
src.visualization.charts.passes_completed_passes_p90_barplot(player_statistics)


print("Charts and statistics have been generated.")


