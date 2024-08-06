def consolve_2d(matrix_a, matrix_b):
    n = len(matrix_a)
    m = len(matrix_a[0])
    k = len(matrix_b)

    # Редактируем размер выходной матрицы
    output_height = n - k + 1
    output_width = m - k + 1
    C = [[0] * output_width for _ in range(output_height)]

    # Выполнием процесс свертки
    # Тут 4 вложенных цикла, мне кажется прога не запустится)
    for i in range(output_height):
        for j in range(output_width):
            sum_value = 0
            for t in range(k):
                for l in range(k):
                    sum_value += matrix_a[i + t][j + l] * matrix_b[t][l]
            C[i][j] = sum_value

    return C

if __name__ == '__main__':
    n, m = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    k = int(input())
    B = [list(map(int, input().split())) for _ in range(k)]

    rezult = consolve_2d(A, B)
    for row in rezult:
        print(" ".join(map(str, row)))
