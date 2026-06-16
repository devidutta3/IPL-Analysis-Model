from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd


# ==================================================
# Load Model
# ==================================================

with open(r"models\model.pkl", "rb") as file:
    model = pickle.load(file)


# ==================================================
# Create FastAPI App
# ==================================================

app = FastAPI(
    title="IPL Score Predictor",
    description="Predict IPL First Innings Score",
    version="1.0"
)


# ==================================================
# Input Schema
# ==================================================

class PredictionRequest(BaseModel):
    batting_team: str
    bowling_team: str
    current_score: int
    wickets_left: int
    overs: float
    current_run_rate: float


# ==================================================
# Home Route
# ==================================================

@app.get("/")
def home():
    return {
        "message": "IPL Score Predictor API Running"
    }


# ==================================================
# Prediction Route
# ==================================================

@app.post("/predict")
def predict_score(data: PredictionRequest):

    input_df = pd.DataFrame(
        [{
            "batting_team": data.batting_team,
            "bowling_team": data.bowling_team,
            "current_score": data.current_score,
            "wickets_left": data.wickets_left,
            "overs": data.overs,
            "current_run_rate": data.current_run_rate
        }]
    )

    prediction = model.predict(input_df)

    return {
        "predicted_score": round(float(prediction[0]), 2)
    }
