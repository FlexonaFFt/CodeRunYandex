# Не является решением задачи
import math
from functools import reduce

def gcd(a, b):
    while b:
        a, b = b, a % b
    return b

def product_of_list(lst):
    product = 1
    for number in lst:
        product *= number
        if product > 10**18:
            product %= 10**18
    return product

def last_nine_digits_of_gcd(a_list, b_list):
    product_a = product_of_list(a_list)
    product_b = product_of_list(b_list)

    final_gcd = gcd(product_a, product_b)
    last_nine_digits = str(final_gcd)[-9:]

    return last_nine_digits.zfill(9)

if __name__ == '__main__':
    n = int(input())
    lst_one = list(map(int, input().split()))
    m = int(input())
    lst_two = list(map(int, input().split()))

    print(last_nine_digits_of_gcd(lst_one, lst_two))
