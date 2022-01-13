from pathlib import Path


def remove_last_char_multiple_files(root_dir):
    files_dir = Path(root_dir)
    for filepath in files_dir.iterdir():
        with open(filepath, 'r') as file:
            content = file.read()
            new_content = content[:-1]

        with open(filepath, 'w') as file:
            file.write(new_content)


def change_content_multiple_files(root_dir, old_str, new_str):
    files_dir = Path(root_dir)

    for filepath in files_dir.iterdir():
        with open(filepath, 'r') as file:
            content = file.read()
            new_content = content.replace(old_str, new_str)

        with open(filepath, 'w') as file:
            file.write(new_content)


remove_last_char_multiple_files('files_backup')
change_content_multiple_files('files_backup', 'amount', 'units')
