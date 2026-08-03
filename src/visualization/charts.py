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

def passes_completed_passes_p90_barplot(df):
    df = df.sort_values(
        by="passes_p90",
        ascending=False
    ).head(10)

    fig, ax = plt.subplots(figsize=(12, 6))

    x = range(len(df))
    width = 0.4

    ax.bar(
        [i - width/2 for i in x],
        df["passes_p90"],
        width,
        label="Passes p90"
    )

    ax.bar(
        [i + width/2 for i in x],
        df["completed_passes_p90"],
        width,
        label="Completed Passes p90"
    )

    ax.set_xticks(x)
    ax.set_xticklabels(
        df["player"],
        rotation=45,
        ha="right"
    )

    ax.set_ylabel("Per 90 minutes")
    ax.set_title("Top Players - Passes p90 vs Completed Passes p90")
    ax.legend()

    plt.tight_layout()
    plt.show()

    def pressures_and_tackles_p90_barplot(df):
        df = df.sort_values(
            by="pressures_p90",
            ascending=False
        ).head(10)

        fig, ax = plt.subplots(figsize=(12, 6))

        x = range(len(df))
        width = 0.4

        ax.bar(
            [i - width/2 for i in x],
            df["pressures_p90"],
            width,
            label="Pressures p90"
        )

        ax.bar(
            [i + width/2 for i in x],
            df["tackles_p90"],
            width,
            label="Tackles p90"
        )

        ax.set_xticks(x)
        ax.set_xticklabels(
            df["player"],
            rotation=45,
            ha="right"
        )

        ax.set_ylabel("Per 90 minutes")
        ax.set_title("Top Players - Pressures p90 vs Tackles p90")
        ax.legend()

        plt.tight_layout()
        plt.show()

    def shots_goals_xg_p90_barplot(df):
        df = df.sort_values(
            by="shots_p90",
            ascending=False
        ).head(10)

        fig, ax = plt.subplots(figsize=(12, 6))

        x = range(len(df))
        width = 0.4

        ax.bar(
            [i - width/2 for i in x],
            df["shots_p90"],
            width,
            label="Shots p90"
        )

        ax.bar(
            [i + width/2 for i in x],
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
        ax.set_title("Top Players - Shots p90 vs Goals p90 vs xG p90")
        ax.legend()

        plt.tight_layout()
        plt.show()  




   