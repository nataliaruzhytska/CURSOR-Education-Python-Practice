import json


def get_data(item_list):
    with open(item_list) as file:
        return json.load(file)


def add_data(data, item_list):
    with open(item_list, mode="w") as file:
        return json.dump(data, file)



