from pymatting.util.util import save_image
from _remove_background import remove_bg_shirts
import _fileio
import _image_processing


def remove_background_pipeline(path, new_path):
        file = _image_processing.open_image(path)
        no_bg = _image_processing.remove_bg_shirts(file)
        _image_processing.save_img(no_bg, new_path)

def crop_pipeline(path, new_path):
    img = _image_processing.open_image(path)
    img = _image_processing.trim(img)
    _image_processing.save_img(img, new_path)

def crop_shirt_pipeline(path, new_path, resize_to):
    img = _image_processing.open_image(path)
    img = _image_processing.trim(img)
    img = _image_processing.resize_image(img, resize_to)
    _image_processing.save_img(img, new_path)

def merge_layers_pipeline(path_background, path_foreground, output):
    bckgrnd = _image_processing.open_image(path_background)
    frgrnd = _image_processing.open_image(path_foreground)
    new_img = _image_processing.add_image_centered(bckgrnd, frgrnd)
    _image_processing.save_img(new_img, output)

def full_shirt_pipeline(path_background: str, path_shirt: str, resize_to: int, output: str):
    bckgrnd = _image_processing.open_image(path_background)
    frgrnd = _fileio.read_image_file(path_shirt)
    frgrnd = remove_bg_shirts(frgrnd)
    frgrnd = _fileio.get_Image(frgrnd)
    frgrnd = _image_processing.auto_crop_image(frgrnd)
    frgrnd = _image_processing.resize_image(frgrnd, resize_to)
    result = _image_processing.add_image_centered(bckgrnd, frgrnd)
    _image_processing.save_img(result, output)
