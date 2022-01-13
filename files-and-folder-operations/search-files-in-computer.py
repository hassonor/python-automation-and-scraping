from pathlib import Path


def search_files(rood_dir_path, search_text):
    root_dir = Path(rood_dir_path)
    search_term = search_text
    for path in root_dir.rglob("*"):
        if search_term in path.stem:
            print(path.absolute())


search_files(".", "14")
