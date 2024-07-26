def main():
    x, y, z = map(int, input().split())
    numbers = str(input())
    availible_digits = set(str(x) + str(y) + str(z))

    if set(numbers).issubset(availible_digits):
        return 0
    else:
        missing_digits = set(numbers) - availible_digits
        return len(set(missing_digits))


if __name__ == '__main__':
    print(main())
