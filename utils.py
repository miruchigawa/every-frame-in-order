import json
import os

def read_json(filename: str) -> list[dict]:
    if not os.path.exists(filename):
        return [] 

    with open(filename, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = [] 

    return data

def write_json(filename: str, data: list[dict]) -> None:
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)