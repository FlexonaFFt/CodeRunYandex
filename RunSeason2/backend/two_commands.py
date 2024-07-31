# Мой вариант ломался на 18 тесте
def solve():
    a = int(input())
    b = int(input())
    n = int(input())

    nn = []
    for iter in range(1, n + 1):
        if (a / iter) > (b / iter):
            nn.append('yep')
        else:
            nn.append("nope")

    if 'nope' not in nn and 'yep' in nn:
        print("YES")
    elif 'yep' in nn:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()

# Верный вариант решения задачи
def f(a, b, n):
    aa = a
    bb = b // n + 1 if (b % n != 0) else b // n
    if aa > bb:
        return "Yes"
    return "No"

def main():
    a = int(input())
    b = int(input())
    n = int(input())
    print(f(a,b,n))

if __name__ == '__main__':
    main()
