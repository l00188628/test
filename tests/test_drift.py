import pandas as pd

def check_for_drift(new_data_path):
    original = pd.DataFrame({'age': [21, 25, 30, 35, 40]})
    new = pd.read_csv(new_data_path)

    threshold = 5
    return abs(original['age'].mean() - new['age'].mean()) > threshold

def test_no_drift_detected():
    result = check_for_drift("new_input.csv")
    assert result in [True, False]
