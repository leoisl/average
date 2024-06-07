def calculate_average(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum // len(numbers)


def main():
    numbers = [2, 4, 6, 8, 10]
    print(calculate_average(numbers))


if __name__ == '__main__':
    main()
