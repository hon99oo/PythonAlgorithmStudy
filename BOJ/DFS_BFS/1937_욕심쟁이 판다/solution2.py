import sys
sys.setrecursionlimit(10**6)


def dfs(x, y):
    if visited[x][y] != 0:
        return
    visited[x][y] = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if graph[nx][ny] > graph[x][y]:
            dfs(nx, ny)
            if visited[x][y] < visited[nx][ny] + 1:
                visited[x][y] = visited[nx][ny] + 1


if __name__ == "__main__":
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dfs(i, j)
    answer = max(map(max, visited))
    print(answer)