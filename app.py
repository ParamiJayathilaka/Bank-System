from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder

app = Flask(__name__)

# Load trained models
with open("svm_model.pkl", "rb") as f:
    svm_model = pickle.load(f)

with open("lr_model.pkl", "rb") as f:
    lr_model = pickle.load(f)

# Load encoders and scalers
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # Convert input into DataFrame
    df_input = pd.DataFrame([data])

    # Apply encoding and scaling
    categorical_cols = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'day_of_week', 'poutcome']
    num_cols = ['age', 'duration', 'campaign', 'pdays', 'previous', 'emp.var.rate', 'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed']

    cat_transformed = encoder.transform(df_input[categorical_cols])
    cat_df = pd.DataFrame(cat_transformed, columns=encoder.get_feature_names_out())

    df_processed = pd.concat([df_input[num_cols], cat_df], axis=1)
    df_scaled = scaler.transform(df_processed)

    # Get predictions
    svm_pred = svm_model.predict(df_scaled)[0]
    lr_pred = lr_model.predict(df_scaled)[0]

    return jsonify({
        "svm_prediction": "yes" if svm_pred == 1 else "no",
        "lr_prediction": "yes" if lr_pred == 1 else "no"
    })

if __name__ == '__main__':
    app.run(debug=True)
