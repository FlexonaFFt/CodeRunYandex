from itertools import product

def min_liars(a, b, c, d):
    reported_queens = [a, b, c, d]
    total_queens = 4
    min_liars = float('inf')

    for distribution in product(range(5), repeat=4):
        if sum(distribution) == total_queens:
            liars = sum(1 for reported, actual in zip(reported_queens, distribution) if reported != actual)
            min_liars = min(min_liars, liars)

    return min_liars

if __name__ == '__main__':
    a, b, c, d = map(int, input().split())
    print(min_liars(a, b, c, d))
