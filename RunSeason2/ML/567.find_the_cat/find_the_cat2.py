import sys

def count_and_label_cats(matrix):
    sys.setrecursionlimit(100000)  # на случай глубоких рекурсий

    M = len(matrix)
    N = len(matrix[0])

    # Матрица для хранения номеров компонентов
    labeled_matrix = [[0] * N for _ in range(M)]
    current_label = 0

    def dfs(x, y, label):
        # Проверка на границы и на то, что мы находимся в компоненте кошки
        if x < 0 or x >= M or y < 0 or y >= N or matrix[x][y] == 0 or labeled_matrix[x][y] != 0:
            return
        # Пометить текущую ячейку текущим лейблом
        labeled_matrix[x][y] = label
        # Рекурсивно проверить все 8 направлений (включая диагонали)
        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            dfs(x + dx, y + dy, label)

    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 1 and labeled_matrix[i][j] == 0:
                current_label += 1
                dfs(i, j, current_label)

    return current_label, labeled_matrix

# Чтение данных из stdin
def read_input():
    input = sys.stdin.read()
    data = input.split()
    M = int(data[0])
    N = int(data[1])
    matrix = []
    index = 2
    for i in range(M):
        row = []
        for j in range(N):
            row.append(int(data[index]))
            index += 1
        matrix.append(row)
    return matrix

if __name__ == "__main__":
    matrix = read_input()
    number_of_cats, labeled_matrix = count_and_label_cats(matrix)

    # Вывод результатов
    print(number_of_cats)
    for row in labeled_matrix:
        print(' '.join(map(str, row)))
