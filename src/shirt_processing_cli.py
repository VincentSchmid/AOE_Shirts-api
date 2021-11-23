import typer
from _remove_background import remove_bg_shirts
import _fileio
from pipelines import *


app = typer.Typer()

@app.command()
def remove_background(path: str, output: str, dry_run: bool = True):
    if _fileio.is_dir(path):
        if not _fileio.is_dir(output):
            typer.echo("output property needs to be a directory")
        else:
            files = _fileio.get_files_in_folder(path)
            
            for file in files:
                new_path = _fileio.replace_suffix(file, "png")
                new_path = _fileio.get_file_in_new_directory(new_path, output)

                typer.echo(f"{file} saving to {new_path}")
                if not dry_run:
                    remove_background_pipeline(file, new_path)

    else:
        if _fileio.is_dir(output):
            new_path = _fileio.get_file_in_new_directory(path, output)
        else:
            new_path = output
        
        remove_background_pipeline(path, new_path)

@app.command()
def crop_images(path: str, output: str, resize: bool = False, resize_to: int = 800, dry_run: bool = True):
    if _fileio.is_dir(path):
        if not _fileio.is_dir(output):
            typer.echo("output property needs to be a directory")
        else:
            files = _fileio.get_files_in_folder(path)

            for file in files:
                new_path = _fileio.replace_suffix(file, "png")
                new_path = _fileio.get_file_in_new_directory(new_path, output)

                if resize:
                    crop_shirt_pipeline(file, new_path, resize_to)
                else:
                    crop_pipeline(file, new_path)

    else:
        if _fileio.is_dir(output):
            new_path = _fileio.get_file_in_new_directory(path, output)
        else:
            new_path = output
        
        typer.echo(f"{path} saving to {new_path}")

        if not dry_run:
            remove_background_pipeline(path, new_path)

@app.command()
def merge_background(path_to_background: str, path_to_foreground: str, output: str):
    if _fileio.is_dir(path_to_foreground):
        if not _fileio.is_dir(output):
            typer.echo("output property needs to be a directory")
        else:
            files = _fileio.get_files_in_folder(path_to_foreground)

            for file in files:
                new_path = _fileio.replace_suffix(file, "png")
                new_path = _fileio.get_file_in_new_directory(new_path, output)
                merge_layers_pipeline(path_to_background, file, new_path)
    
    else:
        if _fileio.is_dir(output):
            new_path = _fileio.get_file_in_new_directory(path_to_foreground, output)
        else:
            new_path = output

            merge_layers_pipeline(path_to_background, path_to_foreground, new_path)

@app.command()
def full_pipeline(path_to_background: str, path_to_foreground: str, output: str, resize_to: int = 900):
    if _fileio.is_dir(path_to_foreground):
        if not _fileio.is_dir(output):
            typer.echo("output property needs to be a directory")
        else:
            files = _fileio.get_files_in_folder(path_to_foreground)

            for file in files:
                new_path = _fileio.replace_suffix(file, "png")
                new_path = _fileio.get_file_in_new_directory(new_path, output)
                full_shirt_pipeline(path_to_background, file, resize_to, new_path)
    
    else:
        if _fileio.is_dir(output):
            new_path = _fileio.get_file_in_new_directory(path_to_foreground, output)
        else:
            new_path = output

        new_path = _fileio.replace_suffix(new_path, "png")
        full_shirt_pipeline(path_to_background, path_to_foreground, resize_to, new_path)

if __name__ == "__main__":
    app()
