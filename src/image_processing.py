from PIL import Image, ImageChops


def open_image(path: str) -> Image:
    return Image.open(path).convert("RGBA")

def auto_crop_image(img: Image) -> Image:
    imageBox = img.getbbox()
    return img.crop(imageBox)

def save_img(img: Image, path: str):
    img.save(path)

def resize_image(img: Image, max_side: int) -> Image:
    return img.thumbnail((max_side, max_side))

def add_image_centered(background: Image, top_image: Image) -> Image:
    position = (background.width // 2 - top_image.width//2, 
                background.height // 2 - top_image.height//2)
    return background.paste(top_image, position, top_image)

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    #Bounding box given as a 4-tuple defining the left, upper, right, and lower pixel coordinates.
    #If the image is completely empty, this method returns None.
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)