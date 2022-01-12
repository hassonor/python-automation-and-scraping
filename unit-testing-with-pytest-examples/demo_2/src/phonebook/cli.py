"""Command Line Interface (CLI) for the Phonebook project.

To populate the phonebook, pass a csv file of data
to stdin, formatted like this:

Name,Phone Number
Bob Smith,0123 45678
...

"""
import csv
import sys

from phonebook.phonenumbers import Phonebook


def determine_consistency(infile):
    book = Phonebook()
    reader = csv.DictReader(infile)
    for row in reader:
        name = row["Name"]
        number = row["Phone Number"]
        book.add(name, number)
    print(f"Phonebook is consistent: {book.is_consistent()}")
    book.clear()


def main():
    """Run the phonebook consistency checking on numbers found in standard input."""
    determine_consistency(sys.stdin)


if __name__ == '__main__':
    main()
