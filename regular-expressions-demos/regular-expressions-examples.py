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


def get_all_emails_from_all_files(root_dir):
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


get_all_emails_from_all_files('files')
