'''
def find_max_proizved():
    lst = list(map(int, input().split()))
    sorted_lst = sorted(lst)
    first_lst = sorted_lst[-3:]
    new_sec_lst = [abs(num) for num in lst]
    second_sorted_lst = sorted(lst)
    second_lst = second_sorted_lst[-3:]

    first_rez = second_rez = 0
    first_rez = first_lst[-3] * first_lst[-2] * first_lst[-1]
    second_rez = second_lst[-3] * second_lst[-2] * second_lst[-1]
    print(second_lst)
    print(first_lst)

    if second_rez > first_rez:
        print(*second_lst)
    else:
        print(*first_lst)

if __name__ == '__main__':
    find_max_proizved()
'''

x = list(map(int, input().split()))

lol = x.copy()

hah = max(lol)
lol.pop(lol.index(hah))

yu = max(lol)
lol.pop(lol.index(yu))

su = max(lol)

lol = x.copy()

y1 = min(lol)
lol.pop(lol.index(min(lol)))

y2 = min(lol)

if y1 * y2 * hah  > hah * yu * su:
    print(y1, y2, hah)
else:
    print(su, yu, hah)
