import json

def fileJsonParser(path):
    with open(path,'r') as file:
        data = json.load(file)
    return data

