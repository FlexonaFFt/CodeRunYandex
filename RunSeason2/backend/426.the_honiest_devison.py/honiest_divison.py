'''
Фактически, цель задачи это искать способ как разделить
строку на равные подстроки таким образом, чтобы это мож
но было сделать максимально эффективно. Например, строк
у "ababbaab" можно разделить как на ["ab" ,"ab","ba","a
b"], так и на ["abab","baab"]. Однако, нас будут интере
совать лишь максимальное кол-во подстрок. Соответсвенно
при такой входной строке ответ будет 4, так как получил
ось максимально эффективно разделить строку на 4 подстр
оки
'''

'''
Решение ломается на 3ем тесте, а их 72+ :)

from collections import Counter

def find_the_honiest_divison(str):
    char_count = Counter(str)
    min_count = min(char_count.values())
    print(min_count)


if __name__ == '__main__':
    string = str(input())
    find_the_honiest_divison(string)
'''

'''
Это решение также ломается на 3ем тесте

def can_divive_string(str):
    char_count = {}
    for char in str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    max_guests = 1
    length = len(str)

    for k in range(1, length + 1):
        if length % k == 0:
            if all(count % k == 0 for count in char_count.values()):
                max_guests = k

    return max_guests

if __name__ == '__main__':
    string = str(input())
    print(can_divive_string(string))
'''

def can_divive_string(str):
    char_count = {}
    for char in str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    can_simple_divive = True
    first_element_count = next(iter(char_count.values()))
    for element_count in char_count.values():
        if element_count != first_element_count:
            can_simple_divive = False
            break

    if can_simple_divive:
        rezult = 1
        length = len(str)

        for k in range(1, length + 1):
            if length % k == 0:
                if all(count % k == 0 for count in char_count.values()):
                    rezult = k
        return rezult
    else:
        rezult = 1
        '''length = len(str)

        for k in range(1, length//2 + 1):
            if length % k == 0:
                substring = str[:k]
                count = length // len(substring)
                if substring * count == str:
                    rezult = max(rezult, count)'''
        return rezult


if __name__ == '__main__':
    string = str(input())
    print(can_divive_string(string))
