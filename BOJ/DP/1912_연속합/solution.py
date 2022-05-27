def solution(array, n):
    dp = [0] * (n)
    dp[0] = array[0]
    max_v = dp[0]
    for i in range(1, n):
        dp[i] = max(array[i], array[i] + dp[i-1])
        if max_v < dp[i]:
            max_v = dp[i]

    return max_v


if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))
    print(solution(array, n))