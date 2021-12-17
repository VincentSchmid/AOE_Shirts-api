from pathlib import Path
import glob
from PIL import Image
import io


def open_image(path: str) -> Image:
    return Image.open(path).convert("RGBA")

def save_img(img: Image, path: str):
    print("saving image")
    img.save(path)

def get_Image(arr) -> Image:
    return Image.open(io.BytesIO(arr)).convert("RGBA")

def image_to_bytes(img:Image) -> bytes:
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return img_byte_arr.getvalue()

def get_files_in_folder(path: str, suffix= "**"):
    return glob.glob(path + f"/**.{suffix}")

def replace_suffix(path: str, suffix: str) -> Path:
    new_filename = Path(path).stem + f".{suffix}"
    return Path(path).parent.joinpath(new_filename)

def get_file_in_new_directory(current_path: str, new_folder: str) -> Path:
    filename = Path(current_path).name
    return Path(new_folder).joinpath(filename)

def is_dir(path: str):
    return Path(path).is_dir()

def save_file(data, path: str):
    f = open(path, "wb+")
    f.write(data)
