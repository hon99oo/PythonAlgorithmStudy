def solution(array, n, k):
    count = 0
    for value in array[::-1]:
        tmp = k//value
        count += tmp
        k -= tmp*value
        if k == 0:
            break

    return count


if __name__ == "__main__":
    n, k = map(int, input().split())
    array = [int(input()) for _ in range(n)]
    print(solution(array, n, k))