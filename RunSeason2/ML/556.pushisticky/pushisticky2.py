def time_mngmnt(m, t, times):
    times = sorted(times)
    total_time = counter = 0

    for time in times:
        if total_time + time <= t:
            total_time += time
            counter += 1
        else:
            break

    return counter

if __name__ == "__main__":
    n, t = map(int, input().split())
    list = map(int, input().split())
    print(time_mngmnt(n, t, list))
