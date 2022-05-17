import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, k, graph_copy):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph_copy[x][y] <= k:
        return False
    graph_copy[x][y] = 0
    dfs(x-1, y, k, graph_copy)
    dfs(x+1, y, k, graph_copy)
    dfs(x, y-1, k, graph_copy)
    dfs(x, y+1, k, graph_copy)
    return True

if __name__ == "__main__":
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    max_v = max(graph[0])
    for g in graph:
        if max_v < max(g):
            max_v = max(g)

    max_g = 0
    for k in range(max_v):
        graph_copy = [g.copy() for g in graph]
        count = 0
        for i in range(n):
            for j in range(n):
                if dfs(i, j, k, graph_copy):
                    count += 1
        if max_g < count:
            max_g = count

    print(max_g)

