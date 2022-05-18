from collections import deque


def bfs(queue,box):
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue
            if box[nx][ny][nz] == -1:
                continue
            if box[nx][ny][nz] == 0:
                queue.append((nx,ny,nz))
                box[nx][ny][nz] = box[x][y][z] + 1


if __name__ == "__main__":
    m, n, h = map(int, input().split())
    box = []
    queue = deque()
    for i in range(h):
        floor = []
        for j in range(n):
            floor.append(list(map(int, input().split())))
            for k in range(m):
                if floor[j][k] == 1:
                    queue.append((i,j,k))
        box.append(floor)

    bfs(queue, box)

    max_count = 0
    for b in box:
        for f in b:
            if f.count(0) >= 1:
                print(-1)
                exit()
            if max_count < max(f):
                max_count = max(f)

    print(max_count - 1)

