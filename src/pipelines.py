from _rembg_helper import remove_bg_shirts
import _fileio
import image_processing


def remove_background_pipeline(path, new_path):
        file = image_processing.open_image(path)
        no_bg = image_processing.trim(file)
        image_processing.save_img(no_bg, new_path)

def crop_pipeline(path, new_path):
    img = image_processing.open_image(path)
    img = image_processing.auto_crop_image(img)
    image_processing.save_img(img, new_path)
