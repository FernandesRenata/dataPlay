# ⚽ DataPlay - Football Data Analysis with StatsBomb

DataPlay is a Python project for football data analysis using the StatsBomb open data API. The project collects match event data, aggregates player statistics throughout an entire competition, creates advanced performance metrics, ranks players by profile, and generates visualizations to support scouting and performance analysis.

## Features

* Retrieve football match data from the StatsBomb Open Data API.
* Select a team from a competition for analysis.
* Calculate season statistics for every player on the selected team.
* Compute per-90-minute metrics for fair player comparison.
* Generate custom performance indicators through feature engineering.
* Rank the top players according to different playing profiles.
* Export all processed data to CSV files.
* Create visualizations for player performance.

---

## Technologies

* Python 3
* Pandas
* StatsBombPy
* Matplotlib

---

## How It Works

### 1. Load Competition Data

The project connects to the StatsBomb Open Data API and downloads all matches from the selected competition and season.

```python
matches = sb.matches(
    competition_id=72,
    season_id=107
)
```

The default dataset is:

* Competition: FIFA Women's World Cup
* Season ID: 107

---

### 2. Team Selection

The user selects a team from the available competition teams.

Example:

```
Choose a team:

0 - Argentina Women's
1 - Australia Women's
2 - Brazil Women's
...
```

Only events involving the selected team are processed.

---

### 3. Match Processing

For every match:

* Download event data
* Filter events for the selected team
* Calculate player statistics
* Calculate minutes played
* Merge both datasets

These statistics are accumulated across the entire season.

---

### 4. Season Aggregation

All player statistics are grouped by:

* Player
* Team

Metrics are summed over every match.

The project currently computes statistics such as:

* Passes
* Completed Passes
* Progressive Passes
* Key Passes
* Assists
* Shots
* Goals
* Expected Goals (xG)
* Expected Assists (xA)
* Dribbles
* Recoveries
* Interceptions
* Pressures
* Tackles
* Minutes Played

---

### 5. Per-90 Metrics

To fairly compare players with different playing times, every metric is normalized per 90 minutes.

For example:

```
Goals per 90
Passes per 90
Pressures per 90
Tackles per 90
```

Formula:

```
Metric per 90 = (Metric / Minutes Played) × 90
```

---

### 6. Feature Engineering

Additional performance indicators are created from the raw statistics.

Examples include:

* Offensive Contribution
* Midfield Contribution
* Defensive Actions

These metrics summarize multiple actions into meaningful player performance scores.

---

### 7. Player Rankings

The project automatically ranks players according to different profiles.

Current rankings include:

### 🛡 Defensive Players

Based on defensive actions such as:

* Tackles
* Recoveries
* Interceptions

---

### 🎯 Attacking Players

Based on:

* Goals
* Assists

---

### 🎮 Midfield Players

Based on:

* Key Passes
* xA
* Dribbles

The Top 3 players in each category are exported as CSV files.

---

## Visualizations

The project currently generates:

### Goals vs Expected Goals (per 90)

Compares actual scoring with expected scoring.

---

### Pressures vs Tackles (per 90)

Highlights defensive activity.

---

### Passes vs Completed Passes (per 90)

Evaluates passing volume and effectiveness.

---

## Output Files

After execution, the following files are generated:

```
team_statistics.csv
player_statistics.csv
top3_attackers.csv
top3_defenders.csv
top3_midfielders.csv
```

These files can be used for further analysis in Excel, Power BI, Tableau, or other visualization tools.

---

## Running the Project

Install the required dependencies:

```bash
pip install pandas matplotlib statsbombpy
```

Run the project:

```bash
python main.py
```

The application will ask for:

1. A player name (optional)
2. A team to analyze

If no player is entered, charts are generated for every player on the selected team.

---

## Future Improvements

Planned features include:

* Player similarity analysis
* Radar charts
* Pass network visualizations
* Shot maps
* Heatmaps
* Position-based comparisons
* Interactive dashboards
* Machine learning models for player evaluation
* Team tactical analysis
* Expected Threat (xT) metrics

---

## Data Source

This project uses the **StatsBomb Open Data** made available through the `statsbombpy` library.

StatsBomb provides free event-level football data for educational and research purposes.

---

## Author

Developed by **Renata Fernandes** as a football analytics project focused on player evaluation, scouting, and data visualization using Python.
