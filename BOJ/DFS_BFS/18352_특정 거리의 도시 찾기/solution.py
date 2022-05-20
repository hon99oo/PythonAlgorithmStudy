from collections import deque


def bfs(s, graph, visited, k):
    queue = deque([s])
    visited[s] = 0
    answer = []
    while queue:
        x = queue.popleft()
        for v in graph[x]:
            if visited[v] == -1:
                visited[v] = visited[x] + 1
                queue.append(v)

    return answer


if __name__ == "__main__":
    n, m, k, x = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [-1] * (n+1)
    for _ in range(m):
        i, j = map(int, input().split())
        graph[i].append(j)

    bfs(x, graph, visited, k)

    flag = False
    for i in range(1, n + 1):
        if visited[i] == k:
            print(i)
            flag = True

    if not flag:
        print(-1)