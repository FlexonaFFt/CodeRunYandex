# Решение неверно
def can_convert(s1 , s2):
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        elif i + 1 < len(s1) and s1[i] == s1[i + 1]:
            i += 1
        elif j + 1 < len(s2) and s2[j] == s2[j + 1]:
            j += 1
        else:
            return False

    while i < len(s1) and i + 1 < len(s1) and s1[i] == s1[i + 1]:
        i += 1
    while j < len(s2) and j + 1 < len(s2) and s2[j] == s2[j + 1]:
        j += 1
    return i == len(s1) and j == len(s2)

def find_common_string(s1, s2, s3):
    for length in range(1, 201):
        for i in range(len(s1) - length + 1):
            common = s1[i:i + length]
            if all(can_convert(s, common) for s in (s1, s2, s3)):
                return common
    return "IMPOSIBLE"

def main():
    import sys
    input = sys.stdin.read
    s1, s2, s3 = input().strip().split()
    rezult = find_common_string(s1, s2, s3)
    print(rezult)

if __name__ == "__main__":
    main()
