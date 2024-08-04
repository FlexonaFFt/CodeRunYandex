def normalize_string(str):
    if not str:
        return str
    normilized = [str[0]]
    for char in str[1:]:
        if char != normilized[-1]:
            normilized.append(char)
    return ''.join(normilized)

def count_transformations(source, target):
    i, j, n, m = 0, 0, len(source), len(target)
    transformations = 0

    while i < n and j < m:
        if source[i] == target[j]:
            i += 1
            j += 1
        elif i + 1 < n and source[i] == source[i + 1]:
            transformations += 1
            i += 2
        elif j + 1 < n and target[j] == target[j + 1]:
            transformations += 1
            j += 2
        else:
            return float('inf')

    transformations += (n - i) // 2
    transformations += (m - j) // 2
    return transformations

def min_transformations(s1, s2, s3):
    norm1, norm2, norm3 = normalize_string(s1), normalize_string(s2), normalize_string(s3)
    if norm1 != norm2 or norm1 != norm3:
        return "IMPOSSIBLE"

    transformations_1 = count_transformations(s1, norm1)
    transformations_2 = count_transformations(s2, norm1)
    transformations_3 = count_transformations(s3, norm1)

    total_transformations = transformations_1 + transformations_2 + transformations_3
    return norm1

if __name__ == '__main__':
    s1 = input()
    s2 = input()
    s3 = input()
    print(min_transformations(s1, s2, s3))
