import pytest
from project import check_word, get_difficulty, load_csv

# def check_word(user_guess, word):

def test_check_word():
    return_string = check_word("zebra", "zebra")
    assert return_string == check_word("zebra", "zebra")

def test_load_csv():

    returned_list = load_csv("subjects/animals.csv")
    assert returned_list == load_csv("subjects/animals.csv")

def test_get_difficulty():
    assert get_difficulty("1") == 1
    assert get_difficulty("invalid_value") == ""