def solution(n):
    dp = [0] * (n+1)
    for i in range(1,n+1):
        dp[i] = i
        j = 1
        while j**2 <= i:
            if dp[i-j**2] + 1 < dp[i]:
                dp[i] = dp[i-j**2] + 1
            j += 1

    return dp[n]


if __name__ == "__main__":
    n = int(input())
    print(solution(n))

