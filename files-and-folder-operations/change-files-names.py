from pathlib import Path

root_dir = Path('files2')
file_paths = root_dir.glob("**/*")

for path in file_paths:
    if path.is_file():
        parent_folder = path.parts
        sub_folders = path.parts[1:-1]

        new_filename = "-".join(sub_folders) + '-' + path.name
        new_filepath = path.with_name(new_filename)  # set the current dir to the correct dir
        path.rename(new_filepath)  # change the filename to new filename in the correct dir
