import os
import re
import requests
from time import sleep
from config import TELEGRAM_KEY, CHAT_ID, FACEBOOK_KEY
from utils import read_json, write_json, remove_directory


def parse_filename_for_time(filename: str) -> str | None:
    match = re.search(r"_time_(\d+)m(\d+)s(\d+)ms", filename)

    if match:
        minutes, seconds, milliseconds = map(int, match.groups())
        return f"{minutes:02d}m{seconds:02d}s{milliseconds:03d}ms"
    else:
        return None


def post_image_telegram(file_path: str, caption: str) -> bool:
    url = f"https://api.telegram.org/bot{TELEGRAM_KEY}/sendPhoto"
    files = {"photo": open(file_path, "rb")}
    data = {"chat_id": CHAT_ID, "caption": caption}
    req = requests.post(url, files=files, data=data)

    res = req.json()
    return res.get("ok", False)


def post_image_facebook(file_path: str, caption: str) -> bool:
    if not FACEBOOK_KEY or FACEBOOK_KEY == "":
        print("Please setup the facebook key on config.py!")
        exit(1)
    url = "https://graph.facebook.com/me/photos"
    files = {"source": open(file_path, "rb")}
    data = {"access_token": FACEBOOK_KEY, "published": 1, "message": caption}
    res = requests.post(url, files=files, data=data)
    print(res.ok)
    print(res.json())
    
    return res.ok
    


def process_image(
    data_frame: dict, dictionary: dict, data_json_path: str, method: str
) -> None:
    timestamp = parse_filename_for_time(dictionary.get("path", ""))
    fps = dictionary.get("max", 0)
    max_frame = max(entry.get("frame", 0) for entry in data_frame)
    info = dictionary.get("info", "No Info")

    caption = f"[{info}] Frame {dictionary.get('frame', 0)} of {max_frame} - Timestamp {timestamp} - Framerate {fps}FPS"
    if (
        post_image_telegram(dictionary.get("path", ""), caption)
        if method == "telegram"
        else post_image_facebook(dictionary.get("path", ""), caption)
    ):
        print(f"Image {dictionary.get('path', '')} successfully posted.")
        os.remove(dictionary.get("path", ""))
        data_frame.remove(dictionary)
        write_json(data_json_path, data_frame)
        print(f"Image {dictionary.get('path', '')} successfully deleted.")


def post_images(foldername: str, method: str = "telegram") -> None:
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
        process_image(data_frame, dictionary, data_json_path, method)
        data_frame = read_json(data_json_path)
        sleep(10)

    remove_directory(foldername)
