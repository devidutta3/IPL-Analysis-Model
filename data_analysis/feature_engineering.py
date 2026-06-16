import pandas as pd


def feature_engineering(matches, deliveries):

    # Merge datasets
    merged_df = pd.merge(
        deliveries,
        matches,
        left_on="match_id",
        right_on="id"
    )

    # Current Score
    merged_df['current_score'] = (
        merged_df
        .groupby(['match_id', 'inning'])['total_runs']
        .cumsum()
    )

    # Wickets Fallen
    merged_df['wickets_fallen'] = (
        merged_df
        .groupby(['match_id', 'inning'])['is_wicket']
        .cumsum()
    )

    # Wickets Left
    merged_df['wickets_left'] = (
        10 - merged_df['wickets_fallen']
    )

    # Overs Played
    merged_df['overs'] = (
        merged_df['over']
        + merged_df['ball'] / 6
    )

    # Current Run Rate
    merged_df['current_run_rate'] = (
        merged_df['current_score']
        / merged_df['overs']
    )

    # Final Score (Target Variable)
    merged_df['final_score'] = (
        merged_df
        .groupby(['match_id', 'inning'])['current_score']
        .transform('max')
    )

    # Keep only first innings
    merged_df = merged_df[
        merged_df['inning'] == 1
    ]

    # Select useful columns
    final_df = merged_df[
        [
            'batting_team',
            'bowling_team',
            'current_score',
            'wickets_left',
            'overs',
            'current_run_rate',
            'final_score'
        ]
    ]

    return final_df


# Load datasets
matches = pd.read_csv(r"data\matches.csv")
deliveries = pd.read_csv(r"data\deliveries.csv")

# Create engineered dataset
result = feature_engineering(matches, deliveries)

# Display information
print(result.head())

print("\n" + "=" * 50)

print(result.info())

print("\n" + "=" * 50)

print(result.shape)
# Create Features (X)
X = result.drop(columns=['final_score'])

# Create Target (y)
y = result['final_score']

print("X Shape:", X.shape)
print("y Shape:", y.shape)

print("\n" + "=" * 50)

print(X.head())

print("\n" + "=" * 50)

print(y.head())

result.to_csv(
    "data/refined_dataset.csv",
    index=False
)
print(result)
print("File Created Successfully ✅")