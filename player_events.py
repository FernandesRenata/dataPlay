import pandas as pd


def count_passes(player_events):
    return (player_events["type"] == "Pass").sum()


def count_completed_passes(player_events):
    return (
        (player_events["type"] == "Pass") &
        (player_events["pass_outcome"].isna())
    ).sum()


def pass_accuracy(player_events):
    total = count_passes(player_events)

    if total == 0:
        return 0

    return round(
        (count_completed_passes(player_events) / total) * 100,
        2
    )


def count_progressive_passes(player_events):
    if "pass_progressive" not in player_events.columns:
        return None

    return (
        (player_events["type"] == "Pass") &
        (player_events["pass_progressive"] == True)
    ).sum()


def count_key_passes(player_events):
    if "pass_shot_assist" not in player_events.columns:
        return None

    return (
        (player_events["type"] == "Pass") &
        (player_events["pass_shot_assist"] == True)
    ).sum()


def count_assists(player_events):
    if "pass_goal_assist" not in player_events.columns:
        return None

    return (
        (player_events["type"] == "Pass") &
        (player_events["pass_goal_assist"] == True)
    ).sum()


def count_shots(player_events):
    return (player_events["type"] == "Shot").sum()


def count_goals(player_events):

    shots = player_events[
        player_events["type"] == "Shot"
    ]

    if "shot_outcome" in shots.columns:
        return (shots["shot_outcome"] == "Goal").sum()

    if "shot_outcome_name" in shots.columns:
        return (shots["shot_outcome_name"] == "Goal").sum()

    return None


def xg(player_events):

    if "shot_statsbomb_xg" not in player_events.columns:
        return None

    return player_events["shot_statsbomb_xg"].fillna(0).sum()


def xa(player_events):

    if "pass_expected_assist" not in player_events.columns:
        return None

    return player_events["pass_expected_assist"].fillna(0).sum()


def count_dribbles(player_events):
    return (player_events["type"] == "Dribble").sum()


def count_recoveries(player_events):
    return (player_events["type"] == "Ball Recovery").sum()


def count_interceptions(player_events):
    return (player_events["type"] == "Interception").sum()


def count_pressures(player_events):
    return (player_events["type"] == "Pressure").sum()


def count_tackles(player_events):
    return (player_events["type"] == "Duel").sum()


def calculate_player(player_events):

    return {
        "player": player_events["player"].iloc[0],
        "team": player_events["team"].iloc[0],

        "passes": count_passes(player_events),
        "completed_passes": count_completed_passes(player_events),
        "pass_accuracy": pass_accuracy(player_events),

        "progressive_passes": count_progressive_passes(player_events),
        "key_passes": count_key_passes(player_events),
        "assists": count_assists(player_events),

        "shots": count_shots(player_events),
        "goals": count_goals(player_events),

        "xG": xg(player_events),
        "xA": xa(player_events),

        "dribbles": count_dribbles(player_events),
        "recoveries": count_recoveries(player_events),
        "interceptions": count_interceptions(player_events),
        "pressures": count_pressures(player_events),
        "tackles": count_tackles(player_events)
    }


def calculate_player_statistics(events):

    statistics = []

    players = (
        events["player"]
        .dropna()
        .unique()
    )

    for player in players:

        player_events = events[
            events["player"] == player
        ]

        statistics.append(
            calculate_player(player_events)
        )

    return pd.DataFrame(statistics)