from pathlib import Path


def extract_files_from_zip(rood_dir_path, files_extensions_to_remove):
    root_dir = Path(rood_dir_path)

    for path in root_dir.glob("*." + files_extensions_to_remove):
        with open(path, 'wb') as file:
            file.write(b'')
        path.unlink()


extract_files_from_zip("empty_files", "txt")
