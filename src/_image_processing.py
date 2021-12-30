from PIL import Image


def open_image(path: str) -> Image:
    return Image.open(path).convert("RGBA")

def auto_crop_image(img: Image) -> Image:
    imageBox = img.getbbox()
    return img.crop(imageBox)

def save_img(img: Image, path: str):
    print("saving image")
    img.save(path)

def resize_image(img: Image, max_side: int) -> Image:
    new_size = resize_dimensions(max_side, img.size)
    return img.resize(tuple(new_size), Image.ANTIALIAS)

def add_image_centered(background: Image, top_image: Image) -> Image:
    position = (background.width // 2 - top_image.width//2, 
                background.height // 2 - top_image.height//2)
    background.paste(top_image, position, top_image)
    return background

def resize_dimensions(max_side:int, dimensions:tuple) -> tuple:
    short_side_ind, long_side_ind = (1, 0) if dimensions[0] > dimensions[1] else (0, 1)
    resize_percentage = (max_side/float(dimensions[long_side_ind]))
    new_short_side = int((float(dimensions[short_side_ind])*float(resize_percentage)))
    new_size = [max_side, max_side]
    new_size[short_side_ind] = new_short_side
    return tuple(new_size)
    