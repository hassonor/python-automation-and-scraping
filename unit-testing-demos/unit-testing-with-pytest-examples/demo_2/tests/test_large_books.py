"""
Load tests with large collections of phone numbers
"""
import csv
import pytest


@pytest.mark.slow
def test_large_file(phonebook):
    with open("sample_data/sample1.csv") as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            name = row["Name"]
            number = row["Phone Number"]
            phonebook.add(name, number)
    assert phonebook.is_consistent()

