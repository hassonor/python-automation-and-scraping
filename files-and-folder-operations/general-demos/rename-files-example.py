from pathlib import Path

# Rename all file in Directory

root_dir = Path('../playground/files')
file_paths = root_dir.iterdir()

for path in file_paths:
    new_filename = "new-" + path.stem + path.suffix
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)
