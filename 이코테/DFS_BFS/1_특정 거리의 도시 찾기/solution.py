from collections import deque

def solution(n, k, x, graph):
    start = x
    visited = [0]*(n+1)

    tmp = bfs(graph, start, visited)
    result = []

    for i,v in enumerate(tmp):
        if v == k:
            result.append(i)

    if len(result) > 0:
        return result
    else:
        return -1

def bfs(graph, start, visited):

    queue = deque([start])
    count = 1
    while queue:
        v = queue.popleft()
        for i in graph:
            if i[0] == v and visited[i[1]] == 0:
                queue.append(i[1])
                visited[i[1]] = count
        count += 1

    return visited

if __name__ == "__main__":
    n = 4
    m = 4
    k = 2
    x = 1
    array = [
        [1, 2],
        [1, 3],
        [2, 3],
        [2, 4]
    ]
    graph = [[] for _ in range(len(array)+1)]
    for i in array:
        graph[i[0]].append(i[1])

    print(solution(n, k, x, graph))