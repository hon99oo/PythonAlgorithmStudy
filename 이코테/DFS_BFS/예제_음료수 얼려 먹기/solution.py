def solution(graph):
    result = 0
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            # 현재 위치에서 DFS 수행
            if dfs(i, j, graph) == True:
                result += 1

    print(result)


def dfs(x, y, graph):

    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= len(graph) or y <= -1 or y >= len(graph[0]):
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y, graph)
        dfs(x, y-1, graph)
        dfs(x+1, y, graph)
        dfs(x, y+1, graph)
        return True

    return False


if __name__ == "__main__":
    graph = [
        [0,0,1,1,0],
        [0,0,0,1,1],
        [1,1,1,1,1],
        [0,0,0,0,0]
    ]

    solution(graph)