from collections import deque


def bfs(x, y, graph):

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            elif graph[nx][ny] == 1:
                graph[nx][ny] += graph[x][y]
                queue.append((nx,ny))


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int,input())))

    bfs(0,0, graph)
    print(graph[n-1][m-1])