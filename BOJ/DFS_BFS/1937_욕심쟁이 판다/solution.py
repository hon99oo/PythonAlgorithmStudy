# bfs로 풀면 시간 초과가 난다!

from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny <0 or ny >= n:
                continue
            if graph[nx][ny] > graph[x][y]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))

    return max(map(max, visited))


if __name__ == "__main__":
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    max_count = 0
    for i in range(n):
        for j in range(n):
            count = bfs(i, j)
            if count > max_count:
                max_count = count
    print(max_count)