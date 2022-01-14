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


def merge_text_files_on_path_to_new_file(root_dir, new_merged_file_name):
    file_dir = Path(root_dir)

    merged = ''
    for filepath in file_dir.iterdir():
        with open(filepath, 'r') as file:
            content = file.read()
        merged = merged + content + '\n'

    with open(new_merged_file_name, 'w') as file:
        file.write(merged)


def merge_text_files_on_path_to_new_file_without_header(root_dir, new_merged_file_name):
    file_dir = Path(root_dir)

    merged = ''
    for index, filepath in enumerate(file_dir.iterdir()):
        with open(filepath, 'r') as file:
            content = file.readlines()
            new_content = content[1:]
        if index == 0:
            content = ''.join(content)
            merged = merged + content + '\n'
        else:
            new_content = ''.join(new_content)
            merged = merged + new_content + '\n'

    with open(new_merged_file_name, 'w') as file:
        file.write(merged)


def replace_headers_first_columns_in_text_file(root_dir, new_headline_columns_for_file, file_name):
    file_dir = Path(root_dir)

    with open(file_name, 'r') as file:
        content = file.readlines()
    content[0] = new_headline_columns_for_file + '\n'

    with open(file_name, 'w') as file:
        file.writelines(content)


remove_last_char_multiple_files('files_backup')
change_content_multiple_files('files_backup', 'amount', 'units')
