from mplsoccer import Pitch
import matplotlib.pyplot as plt
from statsbombpy import sb


def team_heatmap(match_id, team):

    events = sb.events(match_id=match_id)

    team_events = events[
        events["team"] == team
    ]

    team_events = team_events.dropna(subset=["location"])

    team_events["x"] = team_events["location"].apply(lambda p: p[0])
    team_events["y"] = team_events["location"].apply(lambda p: p[1])

    pitch = Pitch(
    pitch_type="statsbomb",
    pitch_color="white",
    line_color="black"
)

    fig, ax = pitch.draw(figsize=(10, 7))

    pitch.kdeplot(
        x=team_events["x"],
        y=team_events["y"],
        ax=ax,
        fill=True,
        cmap="Reds",
        levels=50,
        alpha=0.6,      
        zorder=1         
    )

    pitch.draw(ax=ax)   

    plt.title(team)
    plt.show()