def find_max_proizved():
    lst = list(map(int, input().split()))
    sorted_lst = sorted(lst)
    print(*sorted_lst[-3:])

if __name__ == '__main__':
    find_max_proizved()
