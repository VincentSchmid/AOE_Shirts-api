from fastapi import FastAPI, File
from fastapi.responses import Response
from src._fileio import *
from src.pipelines import full_shirt_pipeline, parameterized_pipeline
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
    return Response(content=img.tobytes(), media_type="image/png")

@app.post("/merge_background/")
async def merge_background(background: bytes=File(...), foreground: bytes=File(...)):
    img = merge_background(get_Image(background), get_Image(foreground))
    return Response(content=img.tobytes(), media_type="image/png")

@app.post("/full_pipeline/")
async def full_pipeline(background: bytes=File(...), foreground: bytes=File(...), resize_to:int=900):
    img = full_shirt_pipeline(get_Image(background),
        get_Image(foreground),
        resize_to)
    return Response(content=img.tobytes(), media_type="image/png")
