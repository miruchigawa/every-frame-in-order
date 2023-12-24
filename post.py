import os
import re
import requests
from time import sleep
from config import TELEGRAM_KEY, CHAT_ID
from utils import read_json, write_json, remove_directory

def parse_filename_for_time(filename: str) -> str | None:
    match = re.search(r'_time_(\d+)m(\d+)s(\d+)ms', filename)

    if match:
        minutes, seconds, milliseconds = map(int, match.groups())
        return f"{minutes:02d}m{seconds:02d}s{milliseconds:03d}ms"
    else:
        return None

def post_image(file_path: str, caption: str) -> bool:
    url = f'https://api.telegram.org/bot{TELEGRAM_KEY}/sendPhoto'
    files = {'photo': open(file_path, 'rb')}
    data = {'chat_id': CHAT_ID, 'caption': caption}
    req = requests.post(url, files=files, data=data)

    res = req.json()
    return res.get("ok", False)

def process_image(data_frame: dict, dictionary: dict, data_json_path: str) -> None:
    timestamp = parse_filename_for_time(dictionary.get('path', ''))
    fps = dictionary.get('max', 0)
    max_frame = max(entry.get('frame', 0) for entry in data_frame)
    
    caption = f"Frame {dictionary.get('frame', 0)} of {max_frame} - Timestamp {timestamp} - Max Framerate {fps}FPS"

    if post_image(dictionary.get('path', ''), caption):
        print(f"Image {dictionary.get('path', '')} successfully posted.")
        os.remove(dictionary.get('path', ''))
        data_frame.remove(dictionary)
        write_json(data_json_path, data_frame)
        print(f"Image {dictionary.get('path', '')} successfully deleted.")

def post_images(foldername: str) -> None:
    if not os.path.exists(foldername):
        print("Folder not found!")
        return

    data_json_path = os.path.join(foldername, "frame.json")
    if not os.path.exists(data_json_path):
        print("frame.json not found. Please export again.")
        remove_directory(foldername)
        return

    data_frame = read_json(data_json_path)
    data_frame_copy = data_frame.copy() 
    
    for dictionary in data_frame_copy:
        process_image(data_frame, dictionary, data_json_path)
        data_frame = read_json(data_json_path)
        sleep(10)
        
    remove_directory(foldername)
