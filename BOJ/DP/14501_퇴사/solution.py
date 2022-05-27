import sys
sys.setrecursionlimit(10**6)


def dfs(depth):
    global sum_max

    if depth == n:
        sum_max = max(sum(answer),sum_max)
        answer.pop()
        return
    elif depth > n:
        answer.pop()
        sum_max = max(sum(answer),sum_max)
        return
    else:
        for i in range(depth, n):
            answer.append(array[i][1])
            dfs(i+array[i][0])

    if len(answer) > 0:
        answer.pop()
    return


if __name__ == "__main__":
    n = int(input())
    array = [tuple(map(int,input().split())) for _ in range(n)]
    sum_max = 0
    for i in range(n):
        answer = []
        dfs(i)
    print(sum_max)