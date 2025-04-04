from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

model = joblib.load('Logistic-Regression.joblib')

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON input
        data = request.get_json()

        print(data)

        # Convert to DataFrame
        input_df = pd.DataFrame([data])

        prediction = model.predict(input_df)

        print(prediction)

        prediction_list = prediction.tolist()

        return jsonify({'prediction': prediction_list[0]})
    
    except Exception as e:
        return jsonify({'error': str(e)})
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)