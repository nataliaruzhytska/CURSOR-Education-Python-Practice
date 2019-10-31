import json
import os


def get_data(data_path="data.json"):
    if os.path.isfile(data_path):
        with open("data.json") as file:
            return json.load(file)
    else:
        return {}
