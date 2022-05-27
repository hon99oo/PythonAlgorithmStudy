def solution(array, n):
    dp = [0] * (n+1)
    for i in range(n-1, -1, -1):
        if i+array[i][0] > n:
            dp[i] = dp[i+1]
        else:
            left = dp[i+1]
            right = dp[i+array[i][0]]+array[i][1]
            dp[i] = max(left, right)
    return dp[0]


if __name__ == "__main__":
    n = int(input())
    array = [tuple(map(int, input().split())) for _ in range(n)]
    print(solution(array, n))