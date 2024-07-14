def main():
    n = int(input())
    nums = list(map(int, input().split()))
    x = int(input())

    closnum = min(nums, key=lambda y: abs(y - x))
    return closnum


if __name__ == '__main__':
    print(main())
