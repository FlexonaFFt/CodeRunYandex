def main():
    lst = list(map(int, input().split()))
    lst_pred = all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))
    if lst_pred:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    print(main())
