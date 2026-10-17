from src.utils import add, average, is_even, capitalize_words


def test_add():
    assert add(2, 3) == 5


def test_average():
    assert average([2, 4, 6]) == 4


def test_average_empty():
    assert average([]) == 0


def test_is_even_true():
    assert is_even(4) is True


def test_is_even_false():
    assert is_even(7) is False


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
