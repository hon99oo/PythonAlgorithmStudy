def solution(n):
    dp = [0,1,1]
    for i in range(3, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]


if __name__ == "__main__":
    n = int(input())
    print(solution(n))