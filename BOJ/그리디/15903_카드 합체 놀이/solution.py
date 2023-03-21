def solution(n, m, arr):
    arr.sort()
    for _ in range(m):
        arr[0] = arr[1] = arr[0] + arr[1]
        arr.sort()

    return sum(arr)


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solution(n, m, arr))