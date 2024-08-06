# Решение не прошло 5 тест
def time_mngmnt(m, t, lst):
    max_counter = 0
    counter = []
    sorted_lst = sorted(lst)
    for push in sorted_lst:
        if push < t:
            counter.append(push)
            if sum(counter) <= t:
                max_counter += 1
    return max_counter


if __name__ == "__main__":
    n, t = map(int, input().split())
    list = map(int, input().split())
    print(time_mngmnt(n, t, list))
