import pathlib
from pathlib import Path
import zipfile


def create_zip_archive(rood_dir_path, archive_name, ):
    root_dir = Path(rood_dir_path)
    archive_path = root_dir / Path(archive_name + '.zip')
    with zipfile.ZipFile(archive_path, 'w') as zf:
        for path in root_dir.rglob("*.txt"):
            zf.write(path)
            # if you want to remove the zipped files'
            # path.unlink() # removing the zipped files


create_zip_archive('zip_files', 'archive')
