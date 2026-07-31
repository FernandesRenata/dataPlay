from statsbombpy import sb
import  pandas as pd

events = sb.events(match_id=3857256)

summary = pd.DataFrame()
passes = events[events["type"] == "Pass"]
shots = events[events["type"] == "Shot"]
fouls = events[events["type"] == "Foul Committed"]
on_target = shots[
    shots["shot_outcome"].isin([
        "Goal",
        "Saved",
        "Saved To Post"
    ])
]
goals = shots[shots["shot_outcome"] == "Goal"]
corners = passes[
    passes["pass_type"] == "Corner"
]
possessions = (
    events.groupby("team")["possession"]
          .nunique()
)
xg = (
    shots.groupby("team")["shot_statsbomb_xg"]
         .sum()
)
accuracy = (
    passes.assign(correct=passes["pass_outcome"].isna())
          .groupby("team")["correct"]
          .mean() * 100
)


summary["Pass"] = passes.groupby("team").size()
summary["Shots"] = shots.groupby("team").size()
summary["On Target"] = on_target.groupby("team").size()
summary["Goals"] = goals.groupby("team").size()
summary["Fouls"] = fouls.groupby("team").size()
summary["Corners"] = corners.groupby("team").size()
summary["xG"] = xg
summary["Pass Accuracy (%)"] = accuracy.round(1)
summary["Possessions"] = possessions


print(summary)