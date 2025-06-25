# 🚗 Car Price Predictor

A machine learning web application that predicts the resale price of a used car based on its features such as model, company, year of purchase, kilometers driven, and fuel type.

## 📌 Project Overview

This project aims to help users estimate the resale value of their used cars using a machine learning model trained on historical car sales data. It combines data preprocessing, model training, and a user-friendly web interface built with Flask.

The key objectives of this project were:

- To apply regression algorithms (Linear Regression and others) to build a predictive model.
- To create an intuitive web interface for users to interact with the model.
- To allow users to select from real values in the dataset for improved prediction accuracy.

## 💡 Features

- Predicts used car resale price
- Input fields for:
  - Car Name
  - Company
  - Year
  - Kilometers Driven
  - Fuel Type
- Uses only valid options from the dataset (drop-downs)
- Clean and responsive user interface
- Background image and custom styling for better UI

## 🛠️ Tech Stack

- **Language**: Python
- **Libraries**: 
  - Pandas, NumPy
  - Scikit-learn
  - Flask
- **Frontend**:
  - HTML, CSS (with a stylish background)
- **Model**: Linear Regression (can be extended to XGBoost, RandomForest, etc.)

## 🚀 How to Run

1. Clone the repo
2. Install requirements:
```
pip install -r requirements.txt
```
3. Run the app:
4. Visit `http://127.0.0.1:5000/` in your browser.

## 🔍 Model Details

- Used `LinearRegression` from `sklearn`
- Pipeline includes one-hot encoding of categorical features
- Optional models like Ridge, Lasso, or XGBoost can be used

## 📦 Future Improvements

- Deploy using Render or Heroku
- Add feature importance and graphs
- Add login system to store user predictions

## 👨‍💻 Author

- **Umaima** – [LinkedIn](https://www.linkedin.com/in/umaima-abdul-rauf-b6375a294/)

---


