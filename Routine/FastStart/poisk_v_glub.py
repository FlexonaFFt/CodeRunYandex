def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def main():
    import sys
    from collections import defaultdict

    data = sys.stdin.read().strip().splitlines()

    # Чтение количества вершин и рёбер
    first_line = data[0].split()
    N = int(first_line[0])
    M = int(first_line[1])

    # Создание графа
    graph = defaultdict(list)

    for line in data[1:]:
        if line.strip():  # Пропускаем пустые строки
            u, v = map(int, line.split())
            graph[u].append(v)
            graph[v].append(u)  # Неориентированный граф

    # Поиск компоненты связности, начиная с вершины 1
    visited = set()
    dfs(graph, 1, visited)

    # Подготовка результата
    result = sorted(visited)
    print(len(result))
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
