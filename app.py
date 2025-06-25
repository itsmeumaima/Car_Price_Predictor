from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
df = pd.read_csv('Final_Car_data.csv')

car_names = sorted(df['name'].unique())
companies = sorted(df['company'].unique())
years = sorted(df['year'].unique(), reverse=True)
fuel_types = sorted(df['fuel_type'].unique())

# Load your trained model
with open('LinearRegressionModel.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html',
                           car_names=car_names,
                           companies=companies,
                           years=years,
                           fuel_types=fuel_types)

@app.route('/predict', methods=['POST'])
def predict():
    # Read form input
    name = request.form['name']
    company = request.form['company']
    year = int(request.form['year'])
    kms_driven = int(request.form['kms_driven'])
    fuel_type = request.form['fuel_type']

    # Prepare input
    input_data = pd.DataFrame([[name, company, year, kms_driven, fuel_type]],
                              columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])

    prediction = model.predict(input_data)[0]
    price = round(prediction, 2)

    return render_template('index.html',
                           prediction_text=f"Estimated Price: ₹{price}",
                           car_names=car_names,
                           companies=companies,
                           years=years,
                           fuel_types=fuel_types)

if __name__ == "__main__":
    app.run(debug=True)