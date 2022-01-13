from pathlib import Path
from datetime import datetime


def add_created_date_to_files(root_path, time_and_date_format):
    root_dir = Path(root_path)
    for path in root_dir.glob("**/*"):
        if path.is_file():
            created_date = datetime.fromtimestamp(path.stat().st_ctime)
            created_date_str = created_date.strftime(time_and_date_format)
            new_filename = created_date_str + '_' + path.name
            new_filepath = path.with_name(new_filename)  # set the current dir to the correct dir
            path.rename(new_filepath)  # change the filename to new filename in the correct dir


add_created_date_to_files('playground/files3', "%Y-%m-%d_%H-%M-%S")
