def make_symmetrical():
    n, counter = int(input()), 0
    numbers = input().split()
    numbers = [int(num) for num in numbers]
    while counter < n - 1:
      length = (n - counter) // 2
      if numbers[counter : counter + length] == numbers[: n - length - 1 : -1]:
        break
      counter += 1
    print(counter)
    print(*numbers[: counter][: : -1])

make_symmetrical()
