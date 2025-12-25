import pytest
from string_utils import StringUtils

utils = StringUtils()

def test_capitalize_normal_word():
    assert utils.capitalize("skypro") == "Skypro"

def test_capitalize_empty_string():
    assert utils.capitalize("") == ""

def test_trim_leading_spaces():
    assert utils.trim("   skypro") == "skypro"

def test_trim_no_spaces():
    assert utils.trim("skypro") == "skypro"

def test_contains_existing_symbol():
    assert utils.contains("SkyPro", "S") is True

def test_contains_missing_symbol():
    assert utils.contains("SkyPro", "U") is False

def test_delete_symbol_single_char():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"

def test_delete_symbol_substring():
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"

def test_delete_symbol_not_found():
    assert utils.delete_symbol("SkyPro", "Z") == "SkyPro"