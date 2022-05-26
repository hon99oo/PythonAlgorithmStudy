def dfs(depth, visited, n):
    global answer

    if depth == n:
        answer.append(visited.copy())
    else:
        for i in range(1, n+1):
            if i in visited:
                continue
            visited[depth] = i
            dfs(depth + 1, visited, n)
            visited[depth] = 0


if __name__ == "__main__":
    n = int(input())
    visited = [0] * n
    answer = []
    dfs(0, visited, n)
    for a in answer:
        print(*a)