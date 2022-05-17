from collections import deque


def bfs(n, visited):
    queue = deque([n])
    visited[n] += 1
    while queue:
        x = queue.popleft()
        if 0 <= x*2 <= 100000:
            if visited[x*2] == 1:
                visited[x*2] += visited[x]
                if x*2 == k:
                    break
                queue.append(x*2)
        if 0 <= x+1 <= 100000:
            if visited[x+1] == 1:
                visited[x+1] += visited[x]
                if x+1 == k:
                    break
                queue.append(x+1)
        if 0 <= x-1 <= 100000:
            if visited[x-1] == 1:
                visited[x-1] += visited[x]
                if x-1 == k:
                    break
                queue.append(x-1)


if __name__ == "__main__":
    n, k = map(int, input().split())
    visited = [1] * 100002
    bfs(n,visited)
    print(visited[k] - 2)