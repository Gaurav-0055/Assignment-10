<div align="center">

# 🫀 Heart Disease Prediction — End-to-End ML Deployment

**AI-ML Assignment 10 — Model Deployment using GitHub & Render**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-REST%20API-000000?style=flat-square&logo=flask&logoColor=white)
![scikit--learn](https://img.shields.io/badge/scikit--learn-RandomForest-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?style=flat-square&logo=render&logoColor=white)
![GitHub](https://img.shields.io/badge/Version%20Control-GitHub-181717?style=flat-square&logo=github&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)

### 🔗 Live Demo
**➡️ [https://assignment-10-ebu7.onrender.com/](https://assignment-10-ebu7.onrender.com/)**

</div>

---

## 👤 Student Details

| Field | Details |
|---|---|
| 🧑 **Name** | Gaurav Gour |
| 🆔 **Registration No.** | 23BSA10096 |
| 📄 **Application No.** | IN26011516 |
| 🏫 **Batch** | 1A |
| 📝 **Assignment** | Assignment - 10 |

---

## 📌 Problem Statement

A healthcare organization wants to deploy a machine learning model that predicts whether a patient is at risk of **heart disease** based on clinical parameters. This project builds that model, wraps it in a REST API, and deploys it as a live, publicly accessible web service.

---

## 📊 Dataset

| Item | Details |
|---|---|
| **Name** | Heart Disease Prediction Dataset |
| **Source** | [Kaggle — johnsmith88/heart-disease-dataset](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset) |
| **Target Variable** | `target` (1 = heart disease present, 0 = absent) |
| **Features** | 13 clinical parameters (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal) |

---

## 🗂️ Project Structure

```
HeartDiseaseDeployment/
│
├── 🐍 app.py               # Flask REST API
├── 📦 model.pkl            # Trained Random Forest model
├── 📄 requirements.txt     # Python dependencies
├── 📘 README.md            # Project documentation
├── 🏋️ train_model.py       # Data preprocessing + model training
├── 📊 heart.csv            # Dataset
├── 🖼️ templates/
│   └── index.html          # (Optional) Browser-based prediction form
└── 🎨 static/
    └── style.css            # (Optional) Form styling
```

---

## ⚙️ How It Works

| Step | Component | Description |
|---|---|---|
| 1️⃣ | `train_model.py` | Loads `heart.csv`, splits data 80/20, trains a Random Forest classifier, evaluates accuracy, saves `model.pkl` |
| 2️⃣ | `app.py` | Loads `model.pkl`, exposes a `/predict` REST endpoint that accepts patient data and returns a JSON prediction |
| 3️⃣ | `templates/index.html` + `static/style.css` | Optional browser form to test predictions without curl/Postman |

---

## 💻 Running Locally

```bash
pip install -r requirements.txt
python train_model.py     # trains and saves model.pkl
python app.py               # starts the API on http://localhost:5000
```

---

## 🔌 API Usage

**Endpoint:** `POST /predict`

**📥 Sample Request**
```json
{
  "age": 52,
  "sex": 1,
  "cp": 0,
  "trestbps": 125,
  "chol": 212,
  "fbs": 0,
  "restecg": 1,
  "thalach": 168,
  "exang": 0,
  "oldpeak": 1.0,
  "slope": 2,
  "ca": 2,
  "thal": 3
}
```

**📤 Sample Response**
```json
{
  "prediction": "Heart Disease Detected"
}
```

---

## ☁️ Deployment on Render

| Setting | Value |
|---|---|
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app` |
| **Live URL** | [https://assignment-10-ebu7.onrender.com/](https://assignment-10-ebu7.onrender.com/) |

---

## 📈 Model Evaluation

| Metric | Score |
|---|---|
| **Algorithm** | Random Forest Classifier |
| **Total Records** | 1,025 |
| **Training Set Shape** | (820, 13) |
| **Testing Set Shape** | (205, 13) |
| **Train/Test Split** | 80% / 20% |
| **Accuracy** | **100.00%** |

---

## ✅ Conclusion

The Random Forest classifier achieved an accuracy of **100.00%** on the held-out test set (205 samples), correctly classifying every patient as either at risk or not at risk of heart disease based on the 13 clinical parameters. While this result is extremely strong, it is also expected for this particular dataset: the commonly used version of the Heart Disease dataset on Kaggle contains a number of duplicate and near-duplicate rows, which makes it comparatively easy for tree-based models like Random Forest to reach very high — and sometimes perfect — accuracy on a random 80/20 split. In a real clinical deployment, this would be treated as a signal to investigate the data further (checking for duplicates, using cross-validation, and testing on a genuinely unseen patient population) rather than accepting the number at face value.

Beyond model performance, the main challenges in this assignment were on the deployment side rather than the modeling side: making sure the Flask API's expected feature order exactly matched the order the model was trained on, keeping the `requirements.txt` versions consistent between the local/Colab environment and Render's build environment, and confirming the deployed service stayed active and reachable during evaluation. Working through these issues highlighted why **MLOps** matters in real-world machine learning: a model is only useful once it can be reliably packaged, version-controlled, served through an API, and kept running in production — and each of those steps introduces its own failure points that are separate from the accuracy of the model itself.

---

<div align="center">

**Made by Gaurav Gour** · AI-ML Assignment 10

</div>
