from collections import deque


def bfs(v, graph, visited):
    queue = deque([v])
    visited[v] += 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 1:
                visited[i] = visited[i] + visited[v]
                queue.append(i)


if __name__ == "__main__":
    n = int(input())
    x, y = map(int, input().split())
    m = int(input())

    visited = [1] * (n+1)
    graph = []
    for _ in range(n+1):
        graph.append([])

    for _ in range(m):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    bfs(x, graph, visited)
    print(visited[y] - 2)