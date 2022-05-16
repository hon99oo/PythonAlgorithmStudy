# 인접 리스트를 활용한 dfs 구현
def dfs(graph, v, visited):

    # 현재 노드를 방문 처리
    visited[v] = True

    # 방문한 노드 출력 및 order list에 저장
    print(v, end=' ')
    order.append(v)

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 인접 행렬을 활용한 dfs 구현
def dfs2(graph, v, visited):

    # 현재 노드를 방문 처리
    visited[v] = True

    # 방문한 노드 출력 및 order list에 저장
    print(v, end=' ')
    order.append(v+1)

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문, value가 1이면 간선으로 연결됨을 뜻함
    for index, value in enumerate(graph[v]):
        if value == 1 and not visited[index]:
            dfs2(graph, index, visited)

if __name__ == "__main__":

    order = []

    # 인접리스트로 그래프 표현
    graph = [
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2, 6, 8],
        [1, 7]
    ]

    # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
    visited = [False] * len(graph)
    dfs(graph, 1, visited)

# -----------------------------------------------------------------

    # 인접행렬로 그래프 표현
    graph = [
        [0, 1, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0]
    ]

    # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
    visited = [False] * len(graph)
    dfs2(graph, 0, visited)
    print(order)
