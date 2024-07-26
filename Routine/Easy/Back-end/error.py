'''
import sys


def main():
    n = int(input())
    prob = []
    for _ in range(n):
        a,b = map(int, input().split())
        prob.append(b / 100)
    total_error_prob = sum(prob)
    for i in range(n):
        print(prob[i] / total_error_prob)

if __name__ == '__main__':
    main()

Работает только для первого ввода данных
'''

import sys


def main():
    def find_probs(n, servers):
        error_probs = [(a * b / 10000) for a, b in servers]
        total_error_probs = sum(error_probs)
        normalized_probs = [p / total_error_probs for p in error_probs]
        return normalized_probs

    n = int(input())
    servers = [tuple(map(int, input().split())) for _ in range(n)]
    probs = find_probs(n, servers)
    for p in probs:
        print(f"{p:.12f}")
        

if __name__ == '__main__':
    main()
