from pymatting.util.util import save_image
from _rembg_helper import remove_bg_shirts
import _fileio
import image_processing


def remove_background_pipeline(path, new_path):
        file = image_processing.open_image(path)
        no_bg = image_processing.remove_bg_shirts(file)
        image_processing.save_img(no_bg, new_path)

def crop_pipeline(path, new_path):
    img = image_processing.open_image(path)
    img = image_processing.trim(img)
    image_processing.save_img(img, new_path)

def crop_shirt_pipeline(path, new_path, resize_to):
    img = image_processing.open_image(path)
    img = image_processing.trim(img)
    img = image_processing.resize_image(img, resize_to)
    image_processing.save_img(img, new_path)

def merge_layers_pipeline(path_background, path_foreground, output):
    bckgrnd = image_processing.open_image(path_background)
    frgrnd = image_processing.open_image(path_foreground)
    new_img = image_processing.add_image_centered(bckgrnd, frgrnd)
    image_processing.save_img(new_img, output)

def full_shirt_pipeline(path_background: str, path_shirt: str, resize_to: int, output: str):
    bckgrnd = image_processing.open_image(path_background)
    frgrnd = _fileio.read_image_file(path_shirt)
    frgrnd = remove_bg_shirts(frgrnd)
    frgrnd = _fileio.get_Image(frgrnd)
    frgrnd = image_processing.auto_crop_image(frgrnd)
    frgrnd = image_processing.resize_image(frgrnd, resize_to)
    result = image_processing.add_image_centered(bckgrnd, frgrnd)
    image_processing.save_img(result, output)
