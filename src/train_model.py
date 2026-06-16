import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)
import pickle
# ==================================================
# Load Refined Dataset
# ==================================================

df = pd.read_csv("data/refined_dataset.csv")

print("Dataset Shape:", df.shape)

# ==================================================
# Features (X) and Target (y)
# ==================================================

X = df.drop(columns=['final_score'])

y = df['final_score']

print("\nX Shape:", X.shape)
print("y Shape:", y.shape)

# ==================================================
# Train Test Split
# ==================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTrain Test Split Completed")

print("X_train:", X_train.shape)
print("X_test :", X_test.shape)

print("y_train:", y_train.shape)
print("y_test :", y_test.shape)

# ==================================================
# Preprocessing
# ==================================================

preprocessor = ColumnTransformer(
    transformers=[
        (
            'teams',
            OneHotEncoder(handle_unknown='ignore'),
            ['batting_team', 'bowling_team']
        )
    ],
    remainder='passthrough'
)

# ==================================================
# Pipeline
# ==================================================

pipeline = Pipeline(
    steps=[
        ('preprocessor', preprocessor),
        ('model', LinearRegression())
    ]
)

# ==================================================
# Train Model
# ==================================================

pipeline.fit(X_train, y_train)

print("\nModel Training Completed Successfully!")

# ==================================================
# Predictions
# ==================================================

predictions = pipeline.predict(X_test)

# ==================================================
# Evaluation Metrics
# ==================================================

r2 = r2_score(y_test, predictions)

mae = mean_absolute_error(
    y_test,
    predictions
)

mse = mean_squared_error(
    y_test,
    predictions
)

rmse = np.sqrt(mse)

# ==================================================
# Results
# ==================================================

print("\n" + "=" * 50)

print("Model Evaluation")

print("=" * 50)

print(f"R² Score : {r2:.4f}")

print(f"MAE      : {mae:.4f}")

print(f"MSE      : {mse:.4f}")

print(f"RMSE     : {rmse:.4f}")



with open(r"models\model.pkl", "wb") as file:
    pickle.dump(pipeline, file)

print("\nModel Saved Successfully!")