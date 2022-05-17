def dfs(x, y, graph):
    global x_count
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == 0:
        return False
    else:
        graph[x][y] = 0
        x_count += 1
        dfs(x+1, y, graph)
        dfs(x-1, y, graph)
        dfs(x, y+1, graph)
        dfs(x, y-1, graph)
        return True


if __name__ == "__main__":
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int,input())))

    total_count = 0
    count_list = []
    global x_count

    for i in range(n):
        for j in range(n):
            x_count = 0
            if dfs(i, j, graph):
                total_count += 1
                count_list.append(x_count)
    count_list.sort()
    print(total_count)
    for c in count_list:
        print(c)
