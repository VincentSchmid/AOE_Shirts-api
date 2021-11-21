import typer
from _rembg_helper import remove_bg_shirts
import _fileio

app = typer.Typer()

def remove_background_pipeline(path, new_path, detail, dry_run):
    if dry_run:
        typer.echo(f"{path} saving to {new_path}")
    else:
        file = _fileio.read_image_file(path)
        no_bg = remove_bg_shirts(file)
        _fileio.save_file(no_bg, new_path)


@app.command()
def remove_background(path: str, output: str, detail: bool = False, dry_run: bool = True):
    if _fileio.is_dir(path):
        if not _fileio.is_dir(output):
            typer.echo("output property needs to be a directory")
        else:
            files = _fileio.get_files_in_folder(path)
            
            for file in files:
                new_path = _fileio.get_file_in_new_directory(file, output)

                remove_background_pipeline(file, new_path, detail, dry_run)

    else:
        if _fileio.is_dir(output):
            new_path = _fileio.get_file_in_new_directory(path, output)
        else:
            new_path = output
        
        remove_background_pipeline(path, new_path, detail, dry_run)


if __name__ == "__main__":
    app()