import requests

APP_ID = "b5a16afc-1"
APP_KEY = "56c7c1120a7ca50f56c134d645e67261-2"

GENDER = "male"
WEIGHT_KG = 102
HEIGHT_CM = 187.96
AGE = 45

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)
