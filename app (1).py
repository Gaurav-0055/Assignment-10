"""
app.py
Task 3 - API Development
Flask REST API that loads the trained model and returns predictions.
Also serves an optional HTML form at "/" via templates/index.html.
"""

from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Load the trained model
model = joblib.load("model.pkl")

# Column order the model was trained on (must match train_model.py output)
FEATURE_ORDER = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal"
]


@app.route("/", methods=["GET"])
def home():
    # Renders templates/index.html if present, otherwise falls back to JSON info
    try:
        return render_template("index.html")
    except Exception:
        return jsonify({
            "message": "Heart Disease Prediction API is running.",
            "usage": "POST patient details as JSON to /predict"
        })


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Supports both a JSON API call and a form submission from index.html
        data = request.get_json(silent=True) or request.form.to_dict()
        data = {k: float(v) for k, v in data.items()}

        input_df = pd.DataFrame([data], columns=FEATURE_ORDER)
        prediction = model.predict(input_df)[0]

        result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease Detected"

        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
