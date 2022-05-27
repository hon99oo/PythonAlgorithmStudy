def solution(array, n):
    dp = [1] * n
    for i in range(1,n):
        for j in range(i-1, -1, -1):
            if array[i] > array[j]:
                dp[i] = max(dp[j] + 1, dp[i])

    return max(dp)


if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))
    print(solution(array, n))