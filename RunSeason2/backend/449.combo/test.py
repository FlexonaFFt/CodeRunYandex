def optimal_cost(n, a, X, b, k, c):
    from collections import Counter

    # Инициализация dp
    dp = [float('inf')] * (k + 1)
    dp[0] = 0

    # Счетчик желаемых товаров
    required = Counter(c)

    # Максимальное количество каждого товара, которое может потребоваться
    max_count = max(required.values())

    # Обработка каждого возможного количества покупок товаров
    for count in range(1, k + 1):
        # Обработка индивидуальных покупок
        for i in range(n):
            if count >= 1:
                dp[count] = min(dp[count], dp[count - 1] + a[i])

        # Обработка покупки комбо
        if count >= 4:
            dp[count] = min(dp[count], dp[count - 4] + X)

    # Подсчет количества каждого товара, необходимого для покупки
    counts = [0] * n
    for item in c:
        counts[item - 1] += 1

    # Итоговая стоимость с учетом комбо и индивидуальных покупок
    total_cost = 0
    for i in range(n):
        if counts[i] > 0:
            total_cost += dp[counts[i]]

    return total_cost

# Ввод данных
n = int(input())
a = list(map(int, input().split()))
x = int(input())
b = list(map(int, input().split()))
k = int(input())
c = list(map(int, input().split()))

# Вызов функции и вывод результата
print(optimal_cost(n, a, x, b, k, c))
