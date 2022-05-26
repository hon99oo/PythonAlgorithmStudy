from collections import deque


def bfs(replica):
    queue = deque()
    for virus in virus_list:
        queue.append(virus)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <0 or nx >= n or ny <0 or ny >= m:
                continue
            if replica[nx][ny] == 0:
                queue.append((nx,ny))
                replica[nx][ny] = 2

    count = 0
    for r in replica:
        count += r.count(0)
    return count


def make_wall(graph, virus_list, blank_list, n, m):
    count_list = []
    blank_length = len(blank_list)
    for i in range(blank_length):
        for j in range(i + 1, blank_length):
            for k in range(j + 1, blank_length):
                replica = []
                for g in graph:
                    replica.append(g.copy())
                replica[blank_list[i][0]][blank_list[i][1]] = 1
                replica[blank_list[j][0]][blank_list[j][1]] = 1
                replica[blank_list[k][0]][blank_list[k][1]] = 1
                count_list.append(bfs(replica))

    return count_list



if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = []
    virus_list = []
    blank_list = []

    for i in range(n):
        graph_row = list(map(int, input().split()))
        graph.append(graph_row)
        for j in range(m):
            if graph[i][j] == 0:
                blank_list.append((i,j))
            elif graph[i][j] == 2:
                virus_list.append((i,j))

    answer = make_wall(graph, virus_list, blank_list, n, m)
    print(max(answer))
