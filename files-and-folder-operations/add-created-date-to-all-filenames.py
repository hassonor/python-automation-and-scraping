from pathlib import Path
from datetime import datetime

root_dir = Path('files3')

for path in root_dir.glob("**/*"):
    if path.is_file():
        created_date = datetime.fromtimestamp(path.stat().st_ctime)
        created_date_str = created_date.strftime("%Y-%m-%d_%H-%M-%S")
        new_filename = created_date_str + '_' + path.name
        new_filepath = path.with_name(new_filename)  # set the current dir to the correct dir
        path.rename(new_filepath)  # change the filename to new filename in the correct dir
