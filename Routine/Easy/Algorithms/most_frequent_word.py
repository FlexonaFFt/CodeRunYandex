# Решение работает неверно для некоторых тестов
''''
import sys

def most_frequent_word(text):
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    max_count = max(word_count.values())
    most_frequent = [word for word, count in word_count.items() if count == max_count]
    return min(most_frequent)

text = input()

if __name__ == '__main__':
    print(most_frequent_word(text)) '''

import sys
 
wordS = (str(sys.stdin.read()).split())
myDict = {}
for word in wordS:
    myDict[word] = myDict.get(word, 0) + 1
maxW = max(myDict.values())
print(min(list(a for a, b in myDict.items() if b == maxW)))
