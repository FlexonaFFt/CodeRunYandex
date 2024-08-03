def maxIdentical(S):
    # Словарь для хранения количества вхождений подстрок
    substring_count = {}

    # Итерация по всем возможным подстрокам
    for i in range(len(S)):
        for j in range(i + 1, len(S) + 1):
            # Получаем подстроку
            substring = S[i:j]
            # Приводим подстроку к стандартному виду (сортируем символы)
            normalized_substring = ''.join(sorted(substring))
            # Увеличиваем счетчик для нормализованной подстроки
            if normalized_substring in substring_count:
                substring_count[normalized_substring] += 1
            else:
                substring_count[normalized_substring] = 1

    # Находим максимальное количество одинаковых подстрок
    max_count = max(substring_count.values(), default=0)
    return max_count

if __name__ == '__main__':
    S = "ogorog"
    res = maxIdentical(S)
    print(res)
