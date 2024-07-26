import sys


def main():
    numbers = input().split()
    numbers = [int(num) for num in numbers]
    sorted_numbers = sorted(numbers)
    print(sorted_numbers[1])

if __name__ == '__main__':
    main()
