import json


def read_json_data(path_to_file):
    with open(path_to_file) as json_data:
        data = json.load(json_data)
        return data
