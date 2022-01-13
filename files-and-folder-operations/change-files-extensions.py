from pathlib import Path


def change_files_extensions_names(rood_dir_path, src_extension, dist_extension):
    root_dir = Path(rood_dir_path)
    for path in root_dir.rglob("*." + src_extension):
        if path.is_file():
            new_filepath = path.with_suffix("." + dist_extension)
            path.rename(new_filepath)


change_files_extensions_names('files4', "txt", "csv")
