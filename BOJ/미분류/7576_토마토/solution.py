from collections import deque


def bfs(queue,box):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if box[nx][ny] == -1:
                continue
            if box[nx][ny] == 0:
                queue.append((nx,ny))
                box[nx][ny] = box[x][y] + 1


if __name__ == "__main__":
    m, n = map(int, input().split())
    box = []
    queue = deque()
    for i in range(n):
        box.append(list(map(int, input().split())))
        for j in range(m):
            if box[i][j] == 1:
                queue.append((i,j))


    bfs(queue, box)

    max_count = 0
    for b in box:
        if b.count(0) >= 1:
            print(-1)
            exit()
        if max_count < max(b):
            max_count = max(b)

    print(max_count - 1)

