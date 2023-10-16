import os
import shutil
from pathlib import Path

import state_bird.data.read as read


def generate_file_path(name, file_type):
    documents_folder = Path(os.path.expanduser("~/Documents"))
    folder_path = documents_folder / 'state_bird_storage' / read.get_project_name()
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_name = f'{name}.{file_type}'
    file_path = folder_path / file_name
    return file_path


def copy_csv_template(name):
    """
    Copies the csv template to the documents folder.
    """
    path = generate_file_path(f"{name}", 'csv')
    shutil.copy('state_bird/codegen/ccw_variable_template.csv', path)
    return True
