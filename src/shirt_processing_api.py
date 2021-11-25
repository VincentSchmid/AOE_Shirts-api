from fastapi import FastAPI, File
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
    return parameterized_pipeline(Image.open(file), 
        remove_background,
        crop_image,
        resize_image,
        resize_to)

@app.post("/merge_background/")
async def merge_background(background: bytes=File(...), foreground: bytes=File(...)):
    return merge_background(Image.open(background), Image.open(foreground))

@app.post("/full_pipeline/")
async def full_pipeline(background: bytes=File(...), foreground: bytes=File(...), resize_to:int=900):
    return full_shirt_pipeline(Image.open(background), Image.open(foreground), resize_to)
