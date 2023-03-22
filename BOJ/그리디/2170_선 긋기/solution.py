def solution(n, arr):
    arr.sort()

    left = arr[0][0]
    right = arr[0][1]

    result = 0
    for k in range(1, n):
        now_left, now_right = arr[k]
        if right > now_left:
            right = max(right, now_right)
        else:
            result += (right - left)
            left, right = now_left, now_right
    result += (right - left)
    return result


if __name__ == "__main__":
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    print(solution(n, arr))