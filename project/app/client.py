import json
import requests

data = {
    "person_age": 30,
    "person_income_log": 10.0,
    "person_home_ownership": "RENT",
    "person_emp_length": 5.0,
    "loan_intent": "DEBT_CONSOLIDATION",
    "loan_grade": "B",
    "loan_amnt": 10000,
    "loan_int_rate": 10.0,
    "loan_percent_income": 0.5,
    "cb_person_default_on_file": 0,
    "cb_person_cred_hist_length": 5
}

response = requests.post("http://localhost:8000/predict", json=data)
print(response.json())