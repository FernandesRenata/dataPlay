import matplotlib.pyplot as plt


def goals_xg_p90_barplot(df, top_n=10):

    df = df.sort_values(
        by="goals_p90",
        ascending=False
    ).head(top_n)

    fig, ax = plt.subplots(figsize=(12, 6))

    x = range(len(df))
    width = 0.4

    ax.bar(
        [i - width/2 for i in x],
        df["goals_p90"],
        width,
        label="Goals p90"
    )

    ax.bar(
        [i + width/2 for i in x],
        df["xG_p90"],
        width,
        label="xG p90"
    )

    ax.set_xticks(x)
    ax.set_xticklabels(
        df["player"],
        rotation=45,
        ha="right"
    )

    ax.set_ylabel("Per 90 minutes")
    ax.set_title("Top Players - Goals p90 vs xG p90")
    ax.legend()

    plt.tight_layout()
    plt.show()


def goals_p90_histogram(df):

    plt.figure(figsize=(10, 6))

    plt.hist(
        df["goals_p90"],
        bins=10,
        edgecolor="black"
    )

    plt.title("Distribution of Goals per 90 Minutes")
    plt.xlabel("Goals per 90")
    plt.ylabel("Number of Players")

    plt.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    plt.show()