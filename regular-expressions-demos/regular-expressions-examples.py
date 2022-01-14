from pathlib import Path
import re

"""
Meta characters:
 .      Matches any single character
 \      Escape one of the meta character to treat it as a regular character
 [...]  Matches a single character or a range that is contained within brackets
        _- -_ order does not matter but without brackets order does matter  
 +      Matches the preceding element one or more times
 ?      Matches the preceding pattern element one or more times
 *      Matches the preceding element zero or more times
 ^      Matches the beginning of a line or string
 $      Matches the end of a line or string
 [^...] Matches a single character or a range that is not contained withing the brackets
 ?:...|... "Or" operator
 {m,n}  Matches the preceding element at least m and not more than n times
 ()     Matches a optional expression

"""


def get_all_emails_from_all_files_with_regex(root_dir):
    files_dir = Path(root_dir)

    for filepath in files_dir.iterdir():
        with open(filepath, 'r') as file:
            content = file.read()
            print(content)
            pattern = re.compile("[^ ]+@[^ ]+\.[a-z]+")
            matches = pattern.findall(content)

        new_file_with_emails = root_dir / Path('emails.txt')
        with open(new_file_with_emails, 'w') as file:
            for email in matches:
                file.write(email + '\n')


def get_all_url_by_regex(file_with_urls, suffix_or_url):
    path = Path(file_with_urls)

    with open(path, 'r') as file:
        content = file.read()
        pattern = re.compile(f"https?://(?:www.)?[^ \n]+\.{suffix_or_url}")
        matches = pattern.findall(content)
        print(matches)


def extract_ip_addresses_with_regex(file_with_ips):
    path = Path(file_with_ips)

    with open(path, 'r') as file:
        content = file.read()
        pattern = re.compile("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}")
        matches = pattern.findall(content)
        print(matches)


def filtering_by_file_name_with_regex(root_dir, str_to_search):
    root_dir = Path(root_dir)
    filenames = root_dir.iterdir()
    filenames_str = [filename.name for filename in filenames]

    pattern = re.compile(f"{str_to_search}[a-z]*-(?:[1-9]|1[0-9]|20).txt", re.IGNORECASE)
    matches = [filename for filename in filenames_str if pattern.findall(filename)]
    print(matches)


# Tests
get_all_url_by_regex('files/urls.txt', "app")
get_all_url_by_regex('files/urls.txt', "com")
extract_ip_addresses_with_regex('files/ip.txt')
filtering_by_file_name_with_regex('files/other-files', 'Jan')

"""
Other Example:

pattern = re.compile(".*Rehovot.*([0|+][0-9]{4,50}|[^ ]+@[^ ]+.[a-z]+)")
    .*Delhi.* searches for Rehovot anywhere in the line.
    [0|+][0-9]{4,50} searches for a 0 or a + followed a number of 4 to 50 digits.
    | makes the preceding and proceeding patterns optional.
    [^ ]+@[^ ]+.[a-z]+ searches for email addresses.
    ( ) are part of the ( | ) "OR" syntax.
"""
