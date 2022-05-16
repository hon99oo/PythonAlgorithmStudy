from collections import deque
import heapq


def dfs(v):
    visited_dfs[v] = True
    order_dfs.append(v)
    while graph[v]:
        i = heapq.heappop(graph[v])
        if not visited_dfs[i]:
            dfs(i)


def bfs(v):
    visited_bfs[v] = True
    order_bfs.append(v)
    queue = deque([v])
    while queue:
        x = queue.popleft()
        while graph_bfs[x]:
            i = heapq.heappop(graph_bfs[x])
            if not visited_bfs[i]:
                visited_bfs[i] = True
                order_bfs.append(i)
                queue.append(i)


if __name__ == "__main__":
    n, m, start = map(int, input().split())
    k = 1
    graph = []
    graph_bfs = []
    for _ in range(n+1):
        graph.append([])
        graph_bfs.append([])

    for _ in range(m):
        x, y = map(int, input().split())
        heapq.heappush(graph[x], y)
        heapq.heappush(graph[y], x)
        heapq.heappush(graph_bfs[x], y)
        heapq.heappush(graph_bfs[y], x)

    visited_dfs = [False] * (n+1)
    order_dfs = []
    visited_bfs = [False] * (n+1)
    order_bfs = []

    dfs(start)
    print(*order_dfs)
    bfs(start)
    print(*order_bfs)