def fibonacci(n):
    dp = [0] * (n+2)
    dp[1] = 1
    dp[2] = 1
    for i in range(3,n+2):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

if __name__ == "__main__":
    n = int(input())
    print(fibonacci(n))