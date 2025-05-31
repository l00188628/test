from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    age = np.array(data['age']).reshape(-1, 1)
    prediction = model.predict(age)
    return jsonify({'predicted_salary': prediction.tolist()[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)