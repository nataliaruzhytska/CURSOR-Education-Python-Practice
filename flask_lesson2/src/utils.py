import json


def get_data(item_list):
    try:
        with open(item_list) as res:
            return json.load(res)
    except(IOError, ValueError, FileNotFoundError, json.JSONDecodeError):
        raise


def add_data(data, item_list):
    try:
        with open(item_list, mode="w") as res:
            return json.dump(data, res)
    except(IOError, FileNotFoundError, ValueError):
        raise

