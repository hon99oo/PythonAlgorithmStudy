from collections import deque


def bfs(s, visited):
    queue = deque([s])
    visited[s] = 1
    while queue:
        x = queue.popleft()
        if x+u <= f:
            if visited[x+u] == 0:
                queue.append(x+u)
                visited[x+u] = visited[x] + 1
                if x+u == g:
                    break
        if x-d > 0:
            if visited[x-d] == 0:
                queue.append(x-d)
                visited[x-d] = visited[x] +1
                if x-d == g:
                    break


if __name__ == "__main__":
    f, s, g, u, d = map(int, input().split())
    visited = [0] * (f+1)
    bfs(s, visited)
    if visited[g] == 0:
        print("use the stairs")
    else:
        print(visited[g]-1)