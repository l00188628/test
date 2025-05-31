import requests

def test_prediction():
    response = requests.post("http://localhost:5000/predict", json={"age": 30})
    assert response.status_code == 200
    assert 'predicted_salary' in response.json()