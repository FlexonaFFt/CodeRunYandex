# Не проходит второй тест
import sys

def count_cats(segmentation):
    rows = len(segmentation)
    cols = len(segmentation[0]) if rows > 0 else 0
    visited = [[False] * cols for _ in range(rows)]
    cat_count = 0
    cat_matrix = [[0] * cols for _ in range(rows)]

    def dfs(x, y, cat_id):
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            if visited[cx][cy]:
                continue
            visited[cx][cy] = True
            cat_matrix[cx][cy] = cat_id

            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if (dx != 0 or dy != 0) and 0 <= cx + dx < rows and 0 <= cy + dy < cols:
                        if segmentation[cx + dx][cy + dy] == 1 and not visited[cx + dx][cy + dy]:
                            stack.append((cx + dx, cy + dy))

    for i in range(rows):
        for j in range(cols):
            if segmentation[i][j] == 1 and not visited[i][j]:
                cat_count += 1
                dfs(i, j, cat_count)

    return cat_count, cat_matrix

if __name__ == "__main__":
    input_data = sys.stdin.read().strip()
    input_matrix = [list(map(int, line.split())) for line in input_data.splitlines()]
    count, output_matrix = count_cats(input_matrix)

    print(count)
    for row in output_matrix:
        print(' '.join(map(str, row)))
