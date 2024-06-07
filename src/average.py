def calculate_average(numbers):
    """
    Calculate the average of a list of numbers
    :param numbers: the list of numbers
    :return: the average of the given numbers
    """
    # Calculate the sum of the numbers
    sum = 0
    for number in numbers:
        sum += number

    # Calculate the average
    amount_of_numbers = len(numbers)

    if amount_of_numbers == 0:
        return -1

    average = sum / amount_of_numbers

    return average


def main():
    numbers = [2, 4, 6, 8, 10]
    average = calculate_average(numbers)
    print(f"The average of {numbers} is {average}")


if __name__ == '__main__':
    main()
