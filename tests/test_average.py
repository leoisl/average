# 3 important cases to test
# 1. Base cases
# 2. General cases
# 3. Edge cases

from src.average import calculate_average


def test_average_one_sized_list():
    numbers = [4]

    actual = calculate_average(numbers)

    expected = 4
    assert actual == expected


def test_two_sized_list():
    numbers = [4, 6]

    actual = calculate_average(numbers)

    expected = 5
    assert actual == expected


def test_zero_sized_list():
    numbers = []

    actual = calculate_average(numbers)
    expected = -1

    assert actual == expected


def test_long_list():
    numbers = [2, 4, 6, 8, 10]

    actual = calculate_average(numbers)
    expected = 6

    assert actual == expected


def test_floating_average():
    numbers = [2, 3]

    actual = calculate_average(numbers)
    expected = 2.5

    assert actual == expected
