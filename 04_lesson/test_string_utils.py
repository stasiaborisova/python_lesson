import pytest
from string_utils import StringUtils

utils = StringUtils()

def test_capitalize_normal_word():
    assert utils.capitalize("skypro") == "Skypro"

def test_capitalize_empty_string():
    assert utils.capitalize("") == ""