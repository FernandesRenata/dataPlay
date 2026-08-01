import pandas as pd

def calculate_minutes(events):

    match_duration = events["minute"].max()

    minutes = {}

    starting = events[
        events["type"] == "Starting XI"
    ]

    for _, row in starting.iterrows():

        lineup = row["tactics"]["lineup"]

        for player in lineup:

            name = player["player"]["name"]

            minutes[name] = match_duration

    substitutions = events[
        events["type"] == "Substitution"
    ]

    for _, row in substitutions.iterrows():

        minute = row["minute"]

        player_out = row["player"]
        player_in = row["substitution_replacement"]

        minutes[player_out] = minute
        minutes[player_in] = match_duration - minute

    return pd.DataFrame({
        "player": minutes.keys(),
        "minutes": minutes.values()
    })

