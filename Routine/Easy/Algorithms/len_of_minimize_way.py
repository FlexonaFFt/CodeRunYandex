# Не получилось решить данную задачу

import sys
from collections import deque

n = int(input())
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
start, end = map(int, input().split())

def searcher(graph, start, end):
    queue = [[start]]
    visited = [False] * len(graph)
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return len(path) - 1
            if not visited[node]:
                visited[node] = True
                for i in range(len(graph)):
                    if graph[node][i] == 1 and not visited[i]:
                        queue.append(path + [i])
    return -1


if __name__ == '__main__':
    print(searcher(graph, start - 1, end - 1))
