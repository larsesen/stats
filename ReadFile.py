import json


def readJsonData(pathToFile):
    with open(pathToFile) as json_data:
        data = json.load(json_data)
        return data
