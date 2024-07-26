'''
import sys


def main():
    n = int(input())
    words = list(map(int, input().split()))
    unique_count = sum(1 for x in set(words) if words.count(x) == 1)
    print(unique_count)

if __name__ == '__main__':
    main()

У этого решения превышен лимит времени
'''

import sys


def main():
    n = int(input())
    a = list(map(int, input().split()))
    freq = {}
    for x in a:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    unique_count = sum(1 for x in freq if freq[x] == 1)
    print(unique_count)

if __name__ == '__main__':
    main()
