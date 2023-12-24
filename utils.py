import json
import os
import shutil

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
        
def remove_directory(directory_path: str) -> None:
    try:
        shutil.rmtree(directory_path)
        print(f"Directory {directory_path} removed successfully.")
    except Exception as e:
        print(f"Failed to remove directory: {e}")