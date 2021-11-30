import os
import requests

url = os.environ["SHIRT_POROCESSING_ADDRESS"]


def full_pipeline(bckgrnd, frgrnd):
    global url
    req_url = url + "?remove_background=on&crop_image=on&resize_image=off"

    payload={}
    files=[
    ('file',('IMG_2578.png',background,'image/png'))
    ]
    headers = {}

    response = requests.request("POST", req_url, headers=headers, data=payload, files=files)

    print(response.text)