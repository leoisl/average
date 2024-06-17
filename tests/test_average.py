from src.average import calculate_average


def test_average_one_sized_list():
    numbers = [4]

    actual = calculate_average(numbers)

    expected = 4
    assert actual == expected


def test_average_empty_list():
    numbers = []

    actual = calculate_average(numbers)

    expected = None
    assert actual == expected


def test_average_general_case():
    numbers = [2, 4, 6, 8, 10]

    actual = calculate_average(numbers)

    expected = 6
    assert actual == expected


def test_average_float_number():
    numbers = [2, 3]

    actual = calculate_average(numbers)

    expected = 2.5
    assert actual == expected


def test_average_negative_numbers():
    numbers = [-2, 2]

    actual = calculate_average(numbers)

    expected = 0
    assert actual == expected

