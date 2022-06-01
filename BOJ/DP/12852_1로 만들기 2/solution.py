def solution(n):
    dp = [-1] * (n+1)
    index = [0] * (n+1)
    for i in range(1,n+1):
        dp[i] = dp[i-1] + 1
        index[i] = (i-1)
        if i%3 == 0:
            if dp[i] > dp[i//3] + 1:
                dp[i] = dp[i//3] + 1
                index[i] = i//3
        if i%2 == 0:
            if dp[i] > dp[i//2] + 1:
                dp[i] = dp[i//2] + 1
                index[i] = i//2
    answer = [n]
    i = n
    while i > 1:
        answer.append(index[i])
        i = index[i]
    return dp[n], answer


if __name__ == "__main__":
    n = int(input())
    min_v, numbers = solution(n)
    print(min_v)
    for number in numbers:
        print(number, end=' ')