from pathlib import Path

root_dir = Path('files')
file_paths = root_dir.glob("**/*")

for path in file_paths:
    if path.is_file():
        parent_folder = path.parts[-2]  # getting folder name
        new_filename = parent_folder + '-' + path.name  # create new filename
        new_filepath = path.with_name(new_filename)  # set the current dir to the correct dir
        path.rename(new_filepath)  # change the filename to new filename in the correct dir
