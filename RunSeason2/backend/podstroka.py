'''
def find_most_common_pair(text):
    pair_freq = {}

    for i in range(len(text) - 1):
        pair = text[i:i+2]
        if pair in pair_freq:
            pair_freq[pair] += 1
        else:
            pair_freq[pair] = 1

    max_freq = max(pair_freq.values())
    most_common_pairs = [pair for pair, frequency in pair_freq.items() if frequency == max_freq]
    print(max(most_common_pairs))

if __name__ == '__main__':
    text = input()
    find_most_common_pair(text)
'''

# Это решение прошло все тесты

def find_podstroka():
    text = input()
    words = text.split()
    pair_counter = {}

    for word in words:
        for i in range(len(word) - 1):
            pair = word[i:i + 2]
            if pair in pair_counter:
                pair_counter[pair] += 1
            else:
                pair_counter[pair] = 1

    max_count = max(pair_counter.values())
    max_pair = max(pair for pair, count in pair_counter.items()
        if count == max_count)
    print(max_pair)

if __name__ == '__main__':
    find_podstroka()
