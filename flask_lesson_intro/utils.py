import json


def get_data():
    try:
        with open("data.json") as file:
            return json.load(file)
    except(IOError, json.JSONDecodeError):
        raise
