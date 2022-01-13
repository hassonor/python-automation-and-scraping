"""Shared fixtures."""

import pytest

from phonebook.phonenumbers import Phonebook


@pytest.fixture
def phonebook(tmpdir):
    """Provides an empty Phonebook"""
    return Phonebook(tmpdir)

