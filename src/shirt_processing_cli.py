import typer
from _rembg_helper import remove_bg_shirts
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
        
        remove_background_pipeline(path, new_path, dry_run)

@app.command()
def crop_images(path: str, output: str, dry_run: bool = True):
    if _fileio.is_dir(path):
        if not _fileio.is_dir(output):
            typer.echo("output property needs to be a directory")
        else:
            files = _fileio.get_files_in_folder(path)

            for file in files:
                new_path = _fileio.replace_suffix(file, "png")
                new_path = _fileio.get_file_in_new_directory(new_path, output)
                crop_pipeline(file, new_path, dry_run)

    else:
        if _fileio.is_dir(output):
            new_path = _fileio.get_file_in_new_directory(path, output)
        else:
            new_path = output
        
        typer.echo(f"{path} saving to {new_path}")

        if not dry_run:
            remove_background_pipeline(path, new_path)


if __name__ == "__main__":
    app()
