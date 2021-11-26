import typer
from src._fileio import *
from src.pipelines import *
from src._image_processing import *


app = typer.Typer()

@app.command()
def advanced_pipeline(path:str,
                 output:str,
                 remove_background:bool=False,
                 crop_image:bool=False,
                 resize_image:bool=False,
                 resize_to:int=900):

    if is_dir(path):
        if not is_dir(output):
            typer.echo("output property needs to be a directory")
        else:
            files = get_files_in_folder(path)
            
            for file in files:
                new_path = replace_suffix(file, "png")
                new_path = get_file_in_new_directory(new_path, output)

                typer.echo(f"{file} saving to {new_path}")
                new_img = parameterized_pipeline(open_image(file), remove_background, crop_image, resize_image, resize_to)
                save_img(new_img, new_path)

    else:
        if is_dir(output):
            new_path = get_file_in_new_directory(path, output)
        else:
            new_path = output
        new_path = replace_suffix(new_path, "png")
        new_img = parameterized_pipeline(open_image(path), remove_background, crop_image, resize_image, resize_to)
        save_img(new_img, new_path)

@app.command()
def remove_background(path: str, output: str, dry_run: bool = True):
    if is_dir(path):
        if not is_dir(output):
            typer.echo("output property needs to be a directory")
        else:
            files = get_files_in_folder(path)
            
            for file in files:
                new_path = replace_suffix(file, "png")
                new_path = get_file_in_new_directory(new_path, output)

                typer.echo(f"{file} saving to {new_path}")
                if not dry_run:
                    new_img = parameterized_pipeline(open_image(file))
                    save_img(new_img, new_path)

    else:
        if is_dir(output):
            new_path = get_file_in_new_directory(path, output)
        else:
            new_path = output
        
        new_img = parameterized_pipeline(open_image(path))
        save_img(new_img, new_path)

@app.command()
def crop_images(path: str, output: str, resize: bool = False, resize_to: int = 800, dry_run: bool = True):
    if is_dir(path):
        if not is_dir(output):
            typer.echo("output property needs to be a directory")
        else:
            files = get_files_in_folder(path)

            for file in files:
                new_path = replace_suffix(file, "png")
                new_path = get_file_in_new_directory(new_path, output)

                new_img = parameterized_pipeline(open_image(file), False, True, resize, resize_to)
                save_img(new_img, new_path)


    else:
        if is_dir(output):
            new_path = get_file_in_new_directory(path, output)
        else:
            new_path = output
        
        typer.echo(f"{path} saving to {new_path}")

        if not dry_run:
            new_img = parameterized_pipeline(open_image(path), False, True, resize, resize_to)
            save_img(new_img, new_path)

@app.command()
def merge_background(path_to_background: str, path_to_foreground: str, output: str):
    if is_dir(path_to_foreground):
        if not is_dir(output):
            typer.echo("output property needs to be a directory")
        else:
            files = get_files_in_folder(path_to_foreground)

            for file in files:
                new_path = replace_suffix(file, "png")
                new_path = get_file_in_new_directory(new_path, output)
                new_img = merge_layers_pipeline(open_image(path_to_background),
                    open_image(file))
                save_img(new_img, new_path)
    
    else:
        if is_dir(output):
            new_path = get_file_in_new_directory(path_to_foreground, output)
        else:
            new_path = output

            new_img = merge_layers_pipeline(open_image(path_to_background), 
                open_image(path_to_foreground))
            save_img(new_img, new_path)

@app.command()
def full_pipeline(path_to_background: str, path_to_foreground: str, output: str, resize_to: int = 900):
    if is_dir(path_to_foreground):
        if not is_dir(output):
            typer.echo("output property needs to be a directory")
        else:
            files = get_files_in_folder(path_to_foreground)

            for file in files:
                new_path = replace_suffix(file, "png")
                new_path = get_file_in_new_directory(new_path, output)

                new_img = full_shirt_pipeline(open_image(path_to_background), 
                    open_image(file), resize_to)
                save_img(new_img, new_path)
    
    else:
        if is_dir(output):
            new_path = get_file_in_new_directory(path_to_foreground, output)
        else:
            new_path = output

        new_path = replace_suffix(new_path, "png")
        new_img = full_shirt_pipeline(open_image(path_to_background), 
            open_image(path_to_foreground), resize_to)
        save_img(new_img, new_path)

if __name__ == "__main__":
    app()
