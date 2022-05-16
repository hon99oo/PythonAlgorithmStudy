def dfs(x, y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

if __name__ == "__main__":
    graph = [
        [0,0,1,1,0],
        [0,0,0,1,1],
        [1,1,1,1,1],
        [0,0,0,0,0]
    ]
    m = len(graph)
    n = len(graph[0])
    count = 0
    for i in range(m):
        for j in range(n):
            if dfs(i, j):
                count += 1

    print(count)