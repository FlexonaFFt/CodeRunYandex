# Тут я просил совета у нейронок, так как не знал что ещё можно сделать.
# Увы, они не помогли)

'''
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
'''

def can_simple_divide(str):
    string = list(str)

    # Count the occurrences of each character
    substring_counts = {}
    for char in range(len(string)):
        substring = "".join(string[:char+1])
        if substring in substring_counts:
            substring_counts[char] = 1
        else:
            substring_counts[char] = 1

    # Check if the string can be divided into equal-length substrings
    # This is a more complex version of the problem
    # We'll check for the maximum number of times the substring can be repeated

    # Check for the most frequent substring
    substring_counts = {}
    for i in range(len(string)):
        substring = string[:i+1]
        # Find the longest repeating substring
        for j in range(len(string)):
            if j < len(string):
                if string[i*j:i*(j+1)] == string[i:i+len(string)-1]:
                    substring_counts[substring] = 1
                    return True
    return False

def main():
    # Example usage
    string = input()

    # Check if the string can be divided into equal-length substrings
    if len(string) % 2 == 0:
        print(True)
    else:
        print(False)

if __name__ == '__main__':
    main()
