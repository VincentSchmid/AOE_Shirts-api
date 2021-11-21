from sys import argv
from pathlib import Path
import glob
from numpy import fromfile


def get_cwd():
    return str(Path.cwd().resolve())

def get_files_in_folder(path, suffix= "**"):
    return glob.glob(path + f"/**.{suffix}")

def get_filename(path):
    return Path(path).name

def get_file_in_new_directory(current_path, new_folder):
    filename = Path(current_path).name
    return Path(new_folder).joinpath(filename)

def is_dir(path):
    return Path(path).is_dir()

def save_file(data, path):
    f = open(path, "wb+")
    f.write(data)

def save_file_to_cwd(filename, data):
    new_path = str(Path.cwd().joinpath(filename).resolve())
    save_file(new_path, data)

def operate_on_files(op, files):
    for file in files:
        op(file)

def read_image_file(path):
    return fromfile(path)

def open_image_and_operate(op, path):
    return op(read_image_file(path))
