from collections import deque


def bfs(start, test, length):
    queue = deque()
    queue.append((start))
    while queue:
        x, y = queue.popleft()
        for i in range(length):
            if not visited[i]:
                if abs(x-test[i][0]) + abs(y-test[i][1]) <= 1000:
                    queue.append(test[i])
                    visited[i] = True
                    if visited[length-1]:
                        return True


if __name__ == "__main__":
    n = int(input())
    tests = []
    starts = []
    ends = []
    for _ in range(n):
        x = []
        m = int(input())
        starts.append(list(map(int, input().split())))
        for _ in range(m+1):
            x.append(list(map(int, input().split())))
        tests.append(x)

    for start, test in zip(starts, tests):
        length = len(test)
        visited = [False] * (length+1)
        if bfs(start, test, length):
            print("happy")
        else:
            print("sad")
