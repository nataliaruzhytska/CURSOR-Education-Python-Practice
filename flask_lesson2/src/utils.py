import json


def get_data(item_list):
    try:
        with open(item_list) as res:
            return json.load(res)
    except(IOError, ValueError, FileNotFoundError, json.JSONDecodeError):
        return []


def add_data(data, item_list):
    try:
        with open(item_list, mode="w") as res:
            return json.dump(data, res)
    except ValueError:
        return item_list


