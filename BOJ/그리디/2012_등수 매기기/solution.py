def solution(n, expectations):
    expectations.sort()
    result = 0
    for i in range(n):
        result += abs(expectations[i]-(i+1))
    return result


if __name__ == "__main__":
    n = int(input())
    expectations = [int(input()) for _ in range(n)]
    print(solution(n, expectations))