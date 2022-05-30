def solution(n):
    dp = [0] * 101
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    for i in range(4,n+1):
        dp[i] = dp[i-2] + dp[i-3]

    return dp


if __name__ == "__main__":
    n = int(input())
    array = [int(input()) for _ in range(n)]
    dp = solution(max(array))
    for a in array:
        print(dp[a])