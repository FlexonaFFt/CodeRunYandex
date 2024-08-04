def get_character_blocks(s):
    if not s:
        return [], []

    chars = [s[0]]
    counts = [1]

    for char in s[1:]:
        if char == chars[-1]:
            counts[-1] += 1
        else:
            chars.append(char)
            counts.append(1)

    return chars, counts

def min_transformations(s1, s2, s3):
    chars1, counts1 = get_character_blocks(s1)
    chars2, counts2 = get_character_blocks(s2)
    chars3, counts3 = get_character_blocks(s3)

    if chars1 != chars2 or chars1 != chars3:
        return "IMPOSSIBLE"

    total_transformations = 0
    result = []

    for i in range(len(chars1)):
        count1, count2, count3 = counts1[i], counts2[i], counts3[i]
        target_count = sorted([count1, count2, count3])[1]

        total_transformations += abs(count1 - target_count)
        total_transformations += abs(count2 - target_count)
        total_transformations += abs(count3 - target_count)

        result.append(chars1[i] * target_count)

    return ''.join(result)

if __name__ == '__main__':
    s1 = input()
    s2 = input()
    s3 = input()
    print(min_transformations(s1, s2, s3))
