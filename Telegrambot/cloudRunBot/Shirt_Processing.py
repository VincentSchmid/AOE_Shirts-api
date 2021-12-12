import os
import requests
from pathlib import Path

url = os.environ["SHIRT_POROCESSING_ADDRESS"]


def full_pipeline(background_filename: str, background_data: bytes, foreground_filename: str, foreground_data: bytes) -> bytes:
    global url
    req_url = url + "/full_pipeline/"

    background_filetype = get_imagetype(background_filename)
    background_filetype = get_imagetype(foreground_filename)

    payload={}
    files=[
        ('background', (background_filename, background_data, f'image/{background_filetype}')),
        ('foreground', (foreground_filename, foreground_data, f'image/{background_filetype}'))
    ]
    headers = {}

    response = requests.request("POST", req_url, headers=headers, data=payload, files=files)

    return response.body


def get_imagetype(filename: str):
    file_ending = Path(filename).suffix
    if file_ending.to_lower() in ["jpeg", "jpg"]:
        return "jpeg"

    if file_ending.to_lower() == "png":
        return "png"
        