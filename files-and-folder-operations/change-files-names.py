from pathlib import Path


def change_files_names_to_parent_and_parent_parent_folders_name(rood_dir_path):
    root_dir = Path(rood_dir_path)
    file_paths = root_dir.glob("**/*")
    for path in file_paths:
        if path.is_file():
            parent_folder = path.parts
            sub_folders = path.parts[1:-1]

            new_filename = "-".join(sub_folders) + '-' + path.name
            new_filepath = path.with_name(new_filename)  # set the current dir to the correct dir
            path.rename(new_filepath)  # change the filename to new filename in the correct dir


change_files_names_to_parent_and_parent_parent_folders_name('files2', )
