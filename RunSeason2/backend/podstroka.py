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
