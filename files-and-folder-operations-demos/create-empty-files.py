from pathlib import Path


def create_empty_files(rood_dir_path, number_of_empty_files, type_extension_files):
    root_dir = Path(rood_dir_path)
    for i in range(number_of_empty_files):
        filename = str(i) + '.' + type_extension_files
        filepath = root_dir / Path(filename)
        filepath.touch()


create_empty_files('playground/empty_files', 40, 'csv')
