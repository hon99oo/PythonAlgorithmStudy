def solution(n, times):
    dp = [times[0] * i for i in range(n+1)]
    length = len(times)
    for i in range(3,n):
        for j in range(length):
            if i-j-1 < j:
                break
            dp[i] = min(dp[i-j-1] + times[j], dp[i])

    return dp[n-1]


if __name__ == "__main__":
    n = 3
    times = [100]
    print(solution(n, times))