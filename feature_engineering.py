import pandas as pd


def create_features(player_statistics):

    df = player_statistics.copy()

    df["passes"] = df["passes"].replace(0, 1)
    df["shots"] = df["shots"].replace(0, 1)
    df["minutes"] = df["minutes"].replace(0, 1)

    df["pass_accuracy"] = (
        df["completed_passes"] /
        df["passes"]
    ) * 100

    df["key_pass_ratio"] = (
        df["key_passes"] /
        df["passes"]
    ) * 100

    df["progressive_pass_ratio"] = (
        df["progressive_passes"] /
        df["passes"]
    ) * 100

    df["goal_conversion"] = (
        df["goals"] /
        df["shots"]
    ) * 100

    df["xg_difference"] = (
        df["goals"] -
        df["xG"]
    )

    df["offensive_contribution"] = (
        df["goals"] +
        df["assists"]
    )

    df["creative_index"] = (
        df["key_passes"] +
        df["xA"]
    )


    df["defensive_actions"] = (
        df["recoveries"] +
        df["interceptions"] +
        df["tackles"]
    )

    df["pressing_actions"] = (
        df["pressures"] +
        df["recoveries"]
    )

    df["ball_actions"] = (
        df["passes"] +
        df["shots"] +
        df["dribbles"] +
        df["recoveries"] +
        df["interceptions"] +
        df["pressures"]
    )

    return df