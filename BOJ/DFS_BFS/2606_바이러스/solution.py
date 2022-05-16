def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


if __name__ == "__main__":
    n = int(input())
    m = int(input())

    graph = []
    for _ in range(n+1):
        graph.append([])

    visited = [False] * (n+1)

    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    dfs(1)
    print(visited.count(True) - 1)