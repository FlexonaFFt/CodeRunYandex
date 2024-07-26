import sys


def main():
    n = int(input())
    spisok = list(map(int, input().split()))
    combinations = {}

    for x in spisok:
        if x in combinations:
            combinations[x] += 1
        else:
            combinations[x] = 1

    max_count = max(combinations.values())
    max_count_nums = [x for x, count in combinations.items() if count == max_count]
    print(max(max_count_nums))

if __name__ == '__main__':
    main()
