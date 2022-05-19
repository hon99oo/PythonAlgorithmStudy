from collections import deque


def solution(r, c, d, graph):
    graph[r][c] = -1
    count = 1
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    queue = deque()
    queue.append((r, c))
    while queue:
        flag = 0
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[(d + i) % 4]
            ny = y + dy[(d + i) % 4]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = -count
                count += 1
                flag = 1
                d = (d+i+1) % 4
                break
        if flag == 0:
            nx = x + dx[(d+1) % 4]
            ny = y + dy[(d+1) % 4]
            if graph[nx][ny] == 1:
                return count
            else:
                graph[nx][ny] = -1
                queue.append((nx, ny))

    return count


if __name__ == "__main__":
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    if d == 1:
        d = 3
    elif d == 3:
        d = 1

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    print(solution(r, c, d, graph))