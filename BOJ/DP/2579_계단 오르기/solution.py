def solution(array, n):
    dp = [0] * (n+1)
    if n >= 1:
        dp[0] = array[0]
    if n >= 2:
        dp[1] = array[1] + array[0]
    if n >= 3:
        dp[2] = max(array[0]+array[2], array[1]+array[2])
        for i in range(3,n):
            left = array[i]+array[i-1]+dp[i-3]
            right = array[i]+dp[i-2]
            dp[i] = max(left, right)
    return dp


if __name__ == "__main__":
    n = int(input())
    array = [int(input()) for _ in range(n)]
    dp = solution(array, n)
    print(dp)
    print(dp[n-1])