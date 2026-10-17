import pytest

from grade_analyzer import (
    calculate_average,
    get_highest_score,
    has_passed,
)


def test_calculate_average():
    assert calculate_average([80, 90, 100]) == 90


def test_calculate_average_with_single_score():
    assert calculate_average([75]) == 75


def test_get_highest_score():
    assert get_highest_score([45, 88, 72]) == 88


def test_has_passed_above_passing_marks():
    assert has_passed(50) is True


def test_has_passed_at_passing_marks():
    assert has_passed(40) is True


def test_empty_scores_raise_error():
    with pytest.raises(ValueError, match="Scores cannot be empty"):
        calculate_average([])