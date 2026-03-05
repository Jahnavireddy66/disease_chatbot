AI Disease Prediction Chatbot

An AI-powered web application that predicts possible diseases based on user-entered symptoms using Machine Learning.
This project combines data preprocessing, symptom encoding, machine learning modeling, and a Flask-based web interface to provide preliminary health guidance.

Project Overview
The system allows users to:
* Enter symptoms in natural language
* Predict the most likely disease
* Receive instant response (< 1 second)
* Get medical advisory guidance
Disclaimer: This system provides informational guidance only and does not replace professional medical consultation.

Machine Learning Approach
Algorithm Used: Random Forest Classifier
Problem Type: Multi-class classification
Feature Engineering: MultiLabelBinarizer for symptom encoding
Model Accuracy: ~83% (Testing Accuracy)
Training Accuracy: ~98%

Project Architecture
Modules:
1. Data Collection Module
2. Data Preprocessing Module
3. Feature Encoding Module
4. Disease Prediction Module
5. Flask Web Backend
6. Chatbot User Interface

Project Structure

disease_chatbot/
│
├── app.py
├── train_model.py
├── Medical DiseaseAndSymptom dataset.xlsx
├── disease_model.pkl
├── symptom_encoder.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md

Technologies Used

Python
Pandas
Scikit-learn
Random Forest
Flask
HTML
CSS
JavaScript

Data Processing
Cleaned symptom text (lowercase, strip spaces)
Removed null values
Combined multiple symptom columns
Converted symptoms to numerical features using MultiLabelBinarizer

Model Training
The model:
Splits dataset into training and testing sets (80-20)
Trains Random Forest classifier
Evaluates performance using Accuracy metric

Evaluation Metrics
Accuracy: ~83%
Fast prediction time (< 1 second)
Good generalization performance



How to Run the Project

Clone the repository
bash
git clone https://github.com/your-username/ai-disease-prediction.git
cd ai-disease-prediction

Create virtual environment
bash
python -m venv venv

Activate environment

Windows:
bash
venv\Scripts\activate

Mac/Linux:
bash
source venv/bin/activate

Install dependencies
bash
pip install -r requirements.txt
Or manually:
bash
pip install flask pandas scikit-learn openpyxl

Train the model
bash
python train_model.py

Run the application
bash
python app.py
Open in browser:
http://127.0.0.1:5000

Example Usage

Input:
cold, cough, sneezing
Output:
Predicted Disease: Allergic Rhinitis

Key Features
Symptom-based disease prediction
Multi-class classification model
Clean conversational UI
Fast response time
Medical advisory disclaimer

Future Improvements
Add Precision, Recall, F1-score evaluation
Handle class imbalance
Deploy on cloud (Heroku / AWS)
Improve chatbot conversation flow
Add multilingual support

