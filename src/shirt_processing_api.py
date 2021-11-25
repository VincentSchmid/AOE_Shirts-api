from fastapi import FastAPI, File
from fastapi.responses import Response
import _fileio
from pipelines import full_shirt_pipeline, parameterized_pipeline
from shirt_processing_cli import remove_background
from PIL import Image


app = FastAPI()

@app.post("/advanced_pipeline/")
async def advanced_pipeline(file: bytes = File(...), 
    remove_bg:bool=True,
    crop_image:bool=False,
    resize_image:bool=False,
    resize_to:int=900):
    img = parameterized_pipeline(file, 
        remove_background,
        crop_image,
        resize_image,
        resize_to)
    print(type(img))
    return Response(content=_fileio.image_to_bytes(img), media_type="image/png")

@app.post("/merge_background/")
async def merge_background(background: bytes=File(...), foreground: bytes=File(...)):
    img = merge_background(_fileio.get_Image(background), _fileio.get_Image(foreground))
    return Response(content=_fileio.image_to_bytes(img), media_type="image/png")

@app.post("/full_pipeline/")
async def full_pipeline(background: bytes=File(...), foreground: bytes=File(...), resize_to:int=900):
    img = full_shirt_pipeline(_fileio.get_Image(background),
        _fileio.get_Image(foreground),
        resize_to)
    return Response(content=_fileio.image_to_bytes(img), media_type="image/png")