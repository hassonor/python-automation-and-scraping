"""Tests for Phonebook class."""

import pytest


@pytest.mark.skip("WIP")
def test_lookup_by_name(phonebook):
    phonebook.add("Bob", "1234")
    assert "1234" == phonebook.lookup("Bob")


def test_phonebook_contains_all_names(phonebook):
    phonebook.add("Bob", "1234")
    assert "Bob" in phonebook.names()


def test_missing_name_raises_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")


def test_empty_phonebook_is_consistent(phonebook):
    assert phonebook.is_consistent()


def test_is_consistent_with_different_entries(phonebook):
    phonebook.add("Bob", "12345")
    phonebook.add("Anna", "012345")
    assert phonebook.is_consistent()


def test_inconsistent_with_duplicate_entries(phonebook):
    phonebook.add("Bob", "12345")
    phonebook.add("Sue", "12345")
    assert not phonebook.is_consistent()


def test_inconsistent_with_duplicate_prefix(phonebook):
    phonebook.add("Bob", "12345")
    phonebook.add("Sue", "123")
    assert not phonebook.is_consistent()

    # skip a test if python is too old example:
    # @pytest.mark.skipif(sys.version_info < (3,6),

    # running all tests except slow
    # @pytest.mark.slow
    # On Terminal: python -m pytest "not slow"

    # Plugins and Other tools for pytest: "https://pypi.org/project/pytest-html/"
