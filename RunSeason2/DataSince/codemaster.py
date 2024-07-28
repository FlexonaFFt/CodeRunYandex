def codemaster(n, lst):
    k = 2
    lst.sort(reverse=True)

    for k in range(1, n + 1):
        if k * k > lst[k - 1]:
            return k - 1
    return n

if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    print(codemaster(n, lst))
