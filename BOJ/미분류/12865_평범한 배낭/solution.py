def solution(stuff, N, K):
    knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

    # 냅색 문제 풀이
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            weight = stuff[i][0]
            value = stuff[i][1]

            if j < weight:
                knapsack[i][j] = knapsack[i - 1][j]  # weight보다 작으면 위의 값을 그대로 가져온다
            else:
                knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

    return knapsack[N][K]


if __name__ == "__main__":
    n, k = map(int, input().split())
    array = [[0,0]]
    for _ in range(n):
        array.append(list(map(int, input().split())))
    print(solution(array, n, k))