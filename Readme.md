# 🏏 IPL Score Predictor

An end-to-end Machine Learning project that predicts the final first-innings score in an IPL match using ball-by-ball match data.

The project uses:

- Python
- Pandas
- NumPy
- Scikit-Learn
- FastAPI
- Linear Regression

---

## 🚀 Project Overview

The goal of this project is to predict the final score of a batting team during the first innings of an IPL match based on the current match situation.

Example:

Current Situation:

- Batting Team: Chennai Super Kings
- Bowling Team: Mumbai Indians
- Current Score: 120
- Wickets Left: 7
- Overs: 15.3
- Current Run Rate: 7.84

Predicted Score:

```text
182 Runs
```

---

## 📊 Dataset

The project uses IPL datasets:

### matches.csv

Contains match-level information:

- Teams
- Venue
- Winner
- Toss Information
- Match Details

### deliveries.csv

Contains ball-by-ball information:

- Batter
- Bowler
- Runs
- Wickets
- Innings Information

---

## 🛠 Tech Stack

### Data Analysis

- Pandas
- NumPy

### Machine Learning

- Scikit-Learn
- Linear Regression

### API Development

- FastAPI
- Uvicorn

### Model Serialization

- Pickle

---

## 🔄 Machine Learning Pipeline

### 1. Dataset Exploration

Performed:

- Data inspection
- Shape analysis
- Column analysis
- Statistical summaries

### 2. Data Cleaning

Performed:

- Missing value analysis
- Duplicate value analysis
- Removal of unnecessary columns

### 3. Feature Engineering

Created:

- Current Score
- Wickets Fallen
- Wickets Left
- Overs Played
- Current Run Rate (CRR)
- Final Score (Target Variable)

### 4. Data Preprocessing

Implemented:

- Train-Test Split
- One-Hot Encoding
- ColumnTransformer

### 5. Model Training

Algorithm:

```python
LinearRegression()
```

### 6. Model Evaluation

Metrics Used:

- R² Score
- MAE
- MSE
- RMSE

---

## 📈 Model Performance

| Metric | Score |
|----------|----------|
| R² Score | 0.5288 |
| MAE | 15.97 |
| MSE | 468.72 |
| RMSE | 21.65 |

Interpretation:

- Average prediction error ≈ 16 runs
- RMSE ≈ 22 runs

---

## 📂 Project Structure

```text
IPL-Analysis-Model/
│
├── data/
│   ├── matches.csv
│   ├── deliveries.csv
│   └── refined_dataset.csv
│
├── models/
│   └── model.pkl
│
├── data_analysis/
│   ├── load_dataset.py
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   └── train_model.py
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd IPL-Analysis-Model
```

### Create Virtual Environment

```bash
python -m venv .env
```

### Activate Environment

Windows:

```bash
.env\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run FastAPI Server

```bash
uvicorn app:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 🔮 Prediction API

### Endpoint

```http
POST /predict
```

### Request Body

```json
{
  "batting_team": "Chennai Super Kings",
  "bowling_team": "Mumbai Indians",
  "current_score": 120,
  "wickets_left": 7,
  "overs": 15.3,
  "current_run_rate": 7.84
}
```

### Response

```json
{
  "predicted_score": 182.45
}
```

---

## 🎯 Future Improvements

- Add Venue Feature
- Add Powerplay Feature
- Add Death Overs Feature
- Add Recent Momentum Features
- Try Random Forest Regressor
- Try XGBoost Regressor
- Build Interactive Frontend
- Deploy on Render/Railway

---

## 👨‍💻 Author

Devidutta Das

Machine Learning & Python Developer

---

## ⭐ If you found this project useful

Give it a star on GitHub.

## 🎨 Frontend Challenge

The Machine Learning model and FastAPI backend are fully implemented and working.

Now here's a challenge for the developer community:

### Challenge

Can you build a beautiful frontend for this IPL Score Predictor?

Requirements:

- Connect with the FastAPI `/predict` endpoint
- Allow users to select:
  - Batting Team
  - Bowling Team
  - Current Score
  - Wickets Left
  - Overs
  - Current Run Rate
- Display the predicted final score
- Responsive design preferred

### Suggested Technologies

- HTML
- CSS
- JavaScript

or

- React.js
- Next.js
- Vue.js
- Angular

### Bonus Points

- Modern UI/UX
- Team Logos
- IPL Theme
- Animations
- Mobile Responsive Design
- Dark Mode Support

### Submission

Fork the repository, build your frontend, and create a Pull Request.

Let's see who can create the best IPL Score Predictor UI! 🏏🚀