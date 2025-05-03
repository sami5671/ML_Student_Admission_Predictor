
![Logo](https://github.com/sami5671/ML_Student_Admission_Predictor/blob/main/frontend/student_admission_predictor/public/logo.png)


# Student Admission Predictor with Smart Recommendation System 

The primary objective of the Student Admission Predictor project is to predict a student’s probability of admission to a university based on key input features: GRE score, TOEFL score, CGPA, and Research experience. The model uses logistic regression, a powerful algorithm for binary classification, to provide accurate predictions of admission chances, helping students understand their likelihood of acceptance into graduate programs. 
## System Architecture of SAPSRS

![App Screenshot](https://github.com/sami5671/ML_Student_Admission_Predictor/blob/main/frontend/student_admission_predictor/public/System%20Diagram.png)
## Installation

### Install Student Admission Predictor with client npm

```bash
  git clone https://github.com/sami5671 ML_Student_Admission_Predictor.git
  
  cd forntend
  cd student_admission_predictor
  npm install 
```

### To Run Client Site

```bash
  npm run dev
```

### To Run Server Site

```bash
  cd backend
  npm install
  nodemon index.js
```

### To Run ML Model

```bash
  cd ml_model
  pip install flask flask-cors pandas matplotlib seaborn numpy
  pip install scikit-learn
  python app.py
```
# Features of Student Admission Predictor
## 🎯 Admission Prediction

This feature uses a logistic regression model to calculate the probability of a student’s university admission. By inputting GRE score, TOEFL score, CGPA, and Research experience, students receive a clear percentage that represents their chance of getting admitted. This prediction helps users make informed decisions based on their academic profile.

## 📊 Feature Contribution Visualization

To help students understand what drives their admission chances, this tool provides a bar chart and box plots showing how much each factor contributes to the final prediction. By visualizing GRE, TOEFL, CGPA, and Research effects, users can identify which areas are strong and which need improvement.

## 💡 Smart Recommendations

Based on the input data and model analysis, the system generates personalized recommendations. If a user’s GRE or CGPA is below optimal levels, they’ll receive clear suggestions for improvement, such as preparing for a retake or gaining research experience. These tips aim to boost admission probabilities.

## Features Vs Admission

![App Screenshot](https://github.com/sami5671/ML_Student_Admission_Predictor/blob/main/frontend/student_admission_predictor/public/feature%20vs%20admission.png)

## Predicted Result With Suggestions

![App Screenshot](https://github.com/sami5671/ML_Student_Admission_Predictor/blob/main/frontend/student_admission_predictor/public/predicted%20result%20and%20suggestion.png)
## Tech Stack

**Client:** React, TailwindCSS

**Server:** Node, Express

**Python:** flask flask-cors pandas matplotlib seaborn numpy scikit-learn

# Author

- [@sami5671](https://www.github.com/sami5671)

