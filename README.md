# 🍷 Drinks Quality Prediction System

An end-to-end **Machine Learning project** that predicts the **quality of drinks** based on their physicochemical properties. The project follows a production-ready modular architecture with data ingestion, validation, transformation, model training, evaluation, and a Flask web application for predictions.

---

## 📌 Project Overview

This project automates the process of predicting drink quality using Machine Learning.

Instead of manually analyzing chemical properties, users can enter the drink's physicochemical attributes through a web interface and receive an instant quality prediction.

The project is built using a complete ML pipeline and follows industry-standard software engineering practices.

---

## 🚀 Features

- End-to-End Machine Learning Pipeline
- Automated Data Ingestion
- Data Validation using Schema
- Data Transformation
- Model Training
- Model Evaluation
- Flask Web Application
- YAML-based Configuration
- Logging
- Modular Project Structure
- Docker Ready Architecture

---

# 🏗️ Project Architecture

```text
                        Dataset
                           │
                           ▼
                  Data Ingestion
                           │
                           ▼
                 Data Validation
                           │
                           ▼
              Data Transformation
                           │
                           ▼
                 Model Training
                           │
                           ▼
                Model Evaluation
                           │
                           ▼
                   Saved Model
                           │
                           ▼
                Prediction Pipeline
                           │
                           ▼
                    Flask Web App
                           │
                           ▼
                   Quality Prediction
```

---

# 📂 Project Structure

```text
Drinks-Quality-Prediction-System
│
├── artifacts/
│
├── config/
│   └── config.yaml
│
├── research/
│
├── src/
│   └── drink_quality_prediction/
│       ├── components/
│       ├── config/
│       ├── constants/
│       ├── entity/
│       ├── pipeline/
│       └── utils/
│
├── static/
├── templates/
│
├── app.py
├── main.py
├── params.yaml
├── schema.yaml
├── setup.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

# ⚙️ Tech Stack

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- Pandas
- NumPy

### Web Framework

- Flask

### Configuration

- YAML

### Model Serialization

- Joblib

### Other Libraries

- Matplotlib
- tqdm
- python-box
- ensure

---

# 📊 Dataset

The project uses a drinks quality dataset containing the following features:

| Feature |
|----------|
| Fixed Acidity |
| Volatile Acidity |
| Citric Acid |
| Residual Sugar |
| Chlorides |
| Free Sulfur Dioxide |
| Total Sulfur Dioxide |
| Density |
| pH |
| Sulphates |
| Alcohol |

### Target Variable

- **Quality**

---

# ⚙️ Pipeline Stages

The training pipeline is divided into five stages.

### Stage 1 — Data Ingestion

- Downloads the dataset
- Extracts the dataset
- Stores it inside the artifacts directory

---

### Stage 2 — Data Validation

- Validates dataset structure
- Checks schema
- Generates validation status

---

### Stage 3 — Data Transformation

- Splits dataset into training and testing sets
- Performs preprocessing
- Saves transformed datasets

---

### Stage 4 — Model Training

- Trains the Machine Learning model
- Saves the trained model as:

```text
artifacts/model_trainer/model.joblib
```

---

### Stage 5 — Model Evaluation

- Evaluates model performance
- Generates evaluation metrics
- Stores metrics in JSON format

---

# 🌐 Flask Application

The project provides a Flask web application with the following routes.

## Home Page

```text
GET /
```

Displays the prediction form.

---

## Train Model

```text
GET /train
```

Runs the complete training pipeline.

Internally executes:

```bash
python main.py
```

---

## Predict

```text
POST /predict
```

Accepts the following inputs:

- Fixed Acidity
- Volatile Acidity
- Citric Acid
- Residual Sugar
- Chlorides
- Free Sulfur Dioxide
- Total Sulfur Dioxide
- Density
- pH
- Sulphates
- Alcohol

Returns the predicted drink quality.

---

# 📁 Configuration Files

## config/config.yaml

Contains:

- Artifact directory
- Dataset URL
- Data paths
- Model paths
- Evaluation paths

---

## schema.yaml

Defines

- Dataset columns
- Data types
- Target column

---

## params.yaml

Stores model hyperparameters.

Current parameters:

```yaml
ElasticNet:
  alpha: 0.2
  l1_ratio: 0.1
```

---

# 🛠️ Installation

## Clone Repository

```bash
git clone https://github.com/sauravyadav7721/Drinks-Quality-Prediction-System.git
```

```bash
cd Drinks-Quality-Prediction-System
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Training Pipeline

```bash
python main.py
```

This executes:

- Data Ingestion
- Data Validation
- Data Transformation
- Model Training
- Model Evaluation

---

# ▶️ Run Flask Application

```bash
python app.py
```

Open:

```
http://localhost:5000
```

---

# 🐳 Docker

Build Docker image:

```bash
docker build -t drinks-quality-prediction .
```

Run Docker container:

```bash
docker run -p 5000:5000 drinks-quality-prediction
```

---

# 📦 Python Dependencies

Main dependencies used in this project:

- pandas
- numpy
- scikit-learn
- matplotlib
- Flask
- Flask-Cors
- PyYAML
- joblib
- tqdm
- ensure
- python-box

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

# 📈 Machine Learning Workflow

```text
Raw Dataset
      │
      ▼
Data Ingestion
      │
      ▼
Data Validation
      │
      ▼
Train-Test Split
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Save Model (.joblib)
      │
      ▼
Prediction Pipeline
      │
      ▼
Flask Application
      │
      ▼
Prediction
```

---

# 💻 Software Engineering Concepts

This project demonstrates:

- Modular Programming
- Object-Oriented Programming
- Configuration Management
- Pipeline Architecture
- Logging
- Exception Handling
- Reusable Components
- YAML Configuration
- Separation of Concerns
- Machine Learning Pipeline Design

---

# 🚀 Future Improvements

- Hyperparameter Tuning
- Cross Validation
- MLflow Integration
- FastAPI Deployment
- Docker Compose
- CI/CD Pipeline
- Cloud Deployment (AWS/Azure/GCP)
- Model Monitoring
- Unit Testing
- Explainable AI (SHAP)

---

# 👨‍💻 Author

**Saurav Yadav**

GitHub: https://github.com/sauravyadav7721

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you find any issues or have ideas to enhance the project, feel free to open an issue or submit a pull request.

---

## ⭐ If you found this project useful

- ⭐ Star this repository
- 🍴 Fork this repository
- 🐛 Report issues
- 📢 Share your feedback

---

## 📄 License

This project is licensed under the **MIT License**.
