from unittest.mock import patch, mock_open
from main import count_titles, count_adult_titles, count_romance_titles, find_title_id, get_rating

# test_assignment.py


def test_count_titles():
    fake_titles = '\n'.join(
        ["1 2 3 4 0 6 7 8 9"]*10 + ["1 2 3 4 1 6 7 8 9"]*5
    )
    with patch("builtins.open", mock_open(read_data=fake_titles)):
        n = count_titles()
    assert n == 15

def test_count_adult_titles():
    fake_titles = '\n'.join(
        ["1 2 3 4 0 6 7 8 9"]*10 + ["1 2 3 4 1 6 7 8 9"]*5
    )
    with patch("builtins.open", mock_open(read_data=fake_titles)):
        n = count_adult_titles()
    assert n == 5

def test_count_romance_titles():
    fake_titles = '\n'.join(
        ["1 2 3 4 0 6 7 8 Romance,abc"]*5 +
        ["1 2 3 4 1 6 7 8 abc,Romance"]*5 +
        ["1 2 3 4 1 6 7 8 abc"]*5
    )
    with patch("builtins.open", mock_open(read_data=fake_titles)):
        n = count_romance_titles()
    assert n == 10

def test_find_title_id():
    fake_titles = '\n'.join(
        ["1 2 3 4 0 6 7 8 Romance,abc"]*5 +
        ["1 2 3 4 1 6 7 8 abc,Romance"]*5 +
        ["t1 t2 t3 t4 t5 t6 t7 t8 t9"] +
        ["1 2 3 4 1 6 7 8 abc"]*5
    )
    with patch("builtins.open", mock_open(read_data=fake_titles)):
        n = find_title_id('t3')
        d = find_title_id('aaa')
    assert n == 't1'
    assert d == ''

def test_get_rating():
    fake_titles = '\n'.join(
        ["1 2 3 4 0 6 7 8 Romance,abc"]*5 +
        ["1 2 3 4 1 6 7 8 abc,Romance"]*5 +
        ["t1 10 t3 t4 t5 t6 t7 t8 t9"] +
        ["1 2 3 4 1 6 7 8 abc"]*5
    )
    with patch("builtins.open", mock_open(read_data=fake_titles)):
        with patch("main.find_title_id", return_value='t1'):
            n = get_rating('t3')
            assert n == '10' or n == 10
        with patch("main.find_title_id", return_value='aaa'):
            d = get_rating('aaa')
            assert d == -1