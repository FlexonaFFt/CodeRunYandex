# Решение прошло 31 тест из 33
# Превышен лимит времени
'''
def check_sequence(sequence):
    count_X = 0
    count_O = 0
    for char in sequence:
        if char == 'X':
            count_X += 1
            count_O = 0
        elif char == 'O':
            count_O += 1
            count_X = 0
        else:
            count_X = 0
            count_O = 0
        if count_X == 5 or count_O == 5:
            return True
    return False

def check_winner(field, n, m):
    for row in field:
        if check_sequence(row):
            return "Yes"

    for col in range(m):
        column_sequence = [field[row][col] for row in range(n)]
        if check_sequence(column_sequence):
            return "Yes"

    for i in range(n):
        for j in range(m):
            if i + 4 < n and j + 4 < m:
                diagonal_sequence = [field[i + k][j + k] for k in range(5)]
                if check_sequence(diagonal_sequence):
                    return "Yes"
            if i + 4 < n and j - 4 >= 0:
                antidiagonal_sequence = [field[i + k][j - k] for k in range(5)]
                if check_sequence(antidiagonal_sequence):
                    return "Yes"

    return "No"

def main():
    n, m = map(int, input().split())
    field = [input().strip() for _ in range(n)]
    print(check_winner(field, n, m))

if __name__ == "__main__":
    main()
'''

# Решение проходит все тесты
# Но только на PyPy

def check_winner(field, n, m):
    for i in range(n):
        for j in range(m):
            if field[i][j] != '.':

                if j + 4 < m:
                    if all(field[i][j + k] == field[i][j] for k in range(5)):
                        return "Yes"

                if i + 4 < n:
                    if all(field[i + k][j] == field[i][j] for k in range(5)):
                        return "Yes"

                if i + 4 < n and j + 4 < m:
                    if all(field[i + k][j + k] == field[i][j] for k in range(5)):
                        return "Yes"

                if i + 4 < n and j - 4 >= 0:
                    if all(field[i + k][j - k] == field[i][j] for k in range(5)):
                        return "Yes"
    return "No"


n, m = map(int, input().split())
field = [input().strip() for _ in range(n)]
print(check_winner(field, n, m))
