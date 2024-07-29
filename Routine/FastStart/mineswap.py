'''
def create_minesweeper_field(N, M, K, mines):
    # Создаем поле, заполненное нулями
    field = [[0 for _ in range(M)] for _ in range(N)]

    # Расставляем мины
    for p, q in mines:
        field[p-1][q-1] = '*'  # Устанавливаем мину
        # Обновляем соседние клетки
        for i in range(max(0, p-2), min(N, p)):
            for j in range(max(0, q-2), min(M, q)):
                if field[i][j] != '*':
                    field[i][j] += 1

    return field

def print_field(field):
    for row in field:
        print(" ".join(str(cell) for cell in row))

N, M, K = map(int, input().split())
mines = [tuple(map(int, input().split())) for _ in range(K)]
field = create_minesweeper_field(N, M, K, mines)
print_field(field)
'''

def create_minesweeper_field(N, M, K, mines):
    field = [[0 for _ in range(M)] for _ in range(N)]
    for p, q in mines:
        field[p-1][q-1] = '*'
    for i in range(N):
        for j in range(M):
            if field[i][j] != '*':
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if 0 <= i+di < N and 0 <= j+dj < M and field[i+di][j+dj] == '*':
                            field[i][j] += 1

    return field

def print_field(field):
    for row in field:
        print(" ".join(str(cell) for cell in row))

N, M, K = map(int, input().split())
mines = [tuple(map(int, input().split())) for _ in range(K)]
field = create_minesweeper_field(N, M, K, mines)
print_field(field)
