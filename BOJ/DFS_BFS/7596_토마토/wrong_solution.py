from collections import deque


def bfs(i,j,k,box):
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    visited = []
    if box[i][j][k] != 1:
        return
    queue = deque([(i,j,k)])
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue
            if (nx, ny, nz) in visited:
                continue
            if box[nx][ny][nz] == 0:
                box[nx][ny][nz] = box[x][y][z] + 1
                queue.append((nx,ny,nz))
                visited.append((nx,ny,nz))
            elif box[nx][ny][nz] != -1:
                if box[nx][ny][nz] >= box[x][y][z] + 1:
                    box[nx][ny][nz] = box[x][y][z] + 1
                    queue.append((nx,ny,nz))


if __name__ == "__main__":
    m, n, h = map(int, input().split())
    box = []
    for _ in range(h):
        floor = []
        for _ in range(n):
            floor.append(list(map(int, input().split())))
        box.append(floor)

    for i in range(h):
        for j in range(n):
            for k in range(m):
                bfs(i,j,k,box)

    max_count = 0
    for b in box:
        for f in b:
            if f.count(0) >= 1:
                print(-1)
                exit()
            if max_count < max(f):
                max_count = max(f)

    print(max_count - 1)

