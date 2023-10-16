import os
from pathlib import Path


def generate_file_path(name, file_type):
    documents_folder = Path(os.path.expanduser("~/Documents"))
    folder_path = documents_folder / 'state_bird_storage'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_name = f'{name}.{file_type}'
    file_path = documents_folder / 'state_bird_storage' / file_name
    return file_path
