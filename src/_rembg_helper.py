import sys
from rembg.bg import remove
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True


def _save_file(data, prop, prop_value):
    f = open(f"{prop}_{prop_value}.jpeg", "wb+")
    f.write(data)

def pipe_out_data(data):
    sys.stdout.buffer.write(data)

def remove_bg(data, amft, ambt, amess):
    return remove(data, alpha_matting=True,
        alpha_matting_foreground_threshold=amft,
        alpha_matting_background_threshold=ambt,
        alpha_matting_erode_structure_size=amess,
        alpha_matting_base_size=200)

def remove_bg_shirts(data):
    return remove_bg(data, amft = 100, ambt = 105, amess = 0)

def test_property(data, amft, ambt, amess, property_name, no_repetitions, increase):
    def incr(amft, ambt, amess, property_name, amount):
        if (property_name == "amft"):
            amft += amount
            property_value = amft
        
        if (property_name == "ambt"):
            ambt += amount
            property_value = ambt
        
        if (property_name == "amess"):
            amess += amount
            property_value = amess
        
        return amft, ambt, amess, property_value

    _, _, _, property_value = incr(amft, ambt, amess, property_name, 0)
    
    for i in range(no_repetitions):
        no_bg = remove_bg(data, amft, ambt, amess)
        _save_file(no_bg, property_name, property_value)
        amft, ambt, amess, property_value = incr(amft, ambt, amess, property_name, increase)

data = sys.stdin.buffer.read()

test_property(data, 1000, 0, 100, "amft", 8, 500)