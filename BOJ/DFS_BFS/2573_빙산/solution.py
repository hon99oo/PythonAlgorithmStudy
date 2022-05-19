from collections import deque

def bfs(x, y):
    global count
    info = []

    queue = deque()
    queue.append((x,y))
    visited[x][y] = True


    dx = [0, 0, 1, -1]
    dy = [1, -1 ,0, 0]

    while queue:
        x, y = queue.popleft()
        count += 1
        water_count = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] > 0:
                queue.append((nx,ny))
                visited[nx][ny] = True
            if graph[nx][ny] == 0:
                water_count += 1
        graph[x][y] -= water_count
        if graph[x][y] < 0:
            graph[x][y] = 0
        if graph[x][y] > 0:
            info.append((x,y))

    return info


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = []
    info = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
        for j in range(m):
            if graph[i][j] > 0:
                info.append((i,j))

    total_count = 0
    flag = 0
    while True:
        visited = [[False] * m for _ in range(n)]
        x, y = info[0]
        length = len(info)
        count = 0
        info = bfs(x, y)
        if length > count:
            break
        if len(info) < 1:
            flag = 1
            break
        total_count += 1
    if flag == 1:
        print(0)
    else:
        print(total_count)



