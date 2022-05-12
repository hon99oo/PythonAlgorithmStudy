def solution(graph, target, start):
    visited = [0]*len(graph)
    count = 0
    dfs(graph, start, visited, count)
    print(visited)

def dfs(graph, v, visited, count):
    visited[v] = count
    for i in graph[v]:
        if v == 1:
            count = 0
        count += 1
        dfs(graph, i, visited, count)

if __name__ == "__main__":
    n, m, k, x = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(n):
        a, b = map(int, input().split())
        graph[a].append(b)

    solution(graph, k, x)