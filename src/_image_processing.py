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
    img.thumbnail((max_side, max_side))
    return img

def add_image_centered(background: Image, top_image: Image) -> Image:
    position = (background.width // 2 - top_image.width//2, 
                background.height // 2 - top_image.height//2)
    background.paste(top_image, position, top_image)
    return background
