'''
from math import gcd

def combinator(n):
    W1, B1 = 1, 1
    W2, B2 = 2, 1
    W3, B3 = 6, 1

    p = 0
    q = 1

    for _ in range(n):
        total1 = W1 + B1
        total2 = W2 + B2
        total3 = W3 + B3

        P_W = (W1 / total1) * (W2 / total2) * (W3 / total3)
        P_B = 1 - P_W

        p += P_W * (q)
        q += P_B * (q)

        B1 += P_B
        B2 += P_B
        B3 += P_B

    common_divisor = gcd(int(p), int(q))
    return int(p // common_divisor), int(q // common_divisor)

if __name__ == '__main__':
    n = int(input())
    p, q = combinator(n)
    print(p, q)
'''

def probability(n):
    P = [0] * (n + 1)
    P[0] = 1/7  # probability of ending in 0 steps
    for i in range(1, n + 1):
        P[i] = 1/7 + (6/7) * P[i-1]
    return P[n]

n = int(input())
p, q = probability(n).as_integer_ratio()
print(p, q)
