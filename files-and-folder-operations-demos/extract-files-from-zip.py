from pathlib import Path
import zipfile


def extract_files_from_zip(rood_dir_path, destination_path):
    root_dir = Path(rood_dir_path)
    destination_path = Path(destination_path)
    for path in root_dir.glob("*.zip"):
        with zipfile.ZipFile(path, 'r') as zf:
            final_path = destination_path / Path(path.stem)
            zf.extractall(path=final_path)


extract_files_from_zip('playground/extract_zip_files', 'playground/extract_zip_files/destination')
