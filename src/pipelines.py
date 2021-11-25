from pymatting.util.util import save_image
from _remove_background import remove_bg_shirts
import _fileio
import _image_processing
from PIL import Image


def parameterized_pipeline(img:Image,
                 remove_bg:bool=True,
                 crop_image:bool=False,
                 resize_image:bool=False,
                 resize_to:int=900) -> Image:

    if remove_bg:
        img = remove_bg_shirts(img)
    if crop_image:
        img = _image_processing.auto_crop_image(img)
    if resize_image:
        img = _image_processing.resize_image(img, resize_to)
    
    return img

def merge_layers_pipeline(bckgrnd:Image, frgrnd:Image) -> Image:
    return _image_processing.add_image_centered(bckgrnd, frgrnd)

def full_shirt_pipeline(bckgrnd: Image, frgrnd: Image, resize_to: int) -> Image:
    img = parameterized_pipeline(frgrnd, True, True, True, resize_to)
    return merge_layers_pipeline(bckgrnd, img)

# _image_processing.open_image(image)
#return _image_processing.save_img(new_img, output)