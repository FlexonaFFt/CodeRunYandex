def weighted_levenshtein_distance(n, m, s, t, I, D, S):
    # Создаем двумерный массив dp размером (n+1) x (m+1)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Инициализация первой строки и первого столбца
    for i in range(1, n + 1):
        dp[i][0] = i * D  # стоимость удаления всех символов из s
    for j in range(1, m + 1):
        dp[0][j] = j * I  # стоимость вставки всех символов в t

    # Заполнение массива dp
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                cost = 0  # символы совпадают, стоимость 0
            else:
                cost = S  # символы различаются, стоимость замены

            dp[i][j] = min(
                dp[i - 1][j] + D,      # удаление
                dp[i][j - 1] + I,      # вставка
                dp[i - 1][j - 1] + cost  # замена
            )

    return dp[n][m]

# Чтение входных данных
n, m = map(int, input().split())
s = input().strip()
t = input().strip()
I, D, S = map(int, input().split())

# Вычисление и вывод результата
result = weighted_levenshtein_distance(n, m, s, t, I, D, S)
print(result)
