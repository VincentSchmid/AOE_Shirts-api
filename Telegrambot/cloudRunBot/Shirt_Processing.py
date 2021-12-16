import os
import requests
from pathlib import Path


def full_pipeline(url, background_filename: str, background_data: bytes, foreground_filename: str, foreground_data: bytes) -> bytes:
    req_url = url + "/full_pipeline/?resize_percentage=93"

    background_filetype = get_imagetype(background_filename)
    background_filetype = get_imagetype(foreground_filename)

    payload={}
    files=[
        ('background', (background_filename, background_data, f'image/{background_filetype}')),
        ('foreground', (foreground_filename, foreground_data, f'image/{background_filetype}'))
    ]
    headers = {}

    response = requests.request("POST", req_url, headers=headers, data=payload, files=files)

    return response.content


def get_imagetype(filename: str):
    file_ending = Path(filename).suffix
    if file_ending.lower() in ["jpeg", "jpg"]:
        return "jpeg"

    if file_ending.lower() == "png":
        return "png"
        