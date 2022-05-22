def upper_bound(start, end, target):
    while start < end:
        mid = (start + end) // 2
        sum_v = sum([a//mid for a in array])
        if sum_v >= target:
            start = mid + 1
        elif sum_v < target:
            end = mid
    mid = (start + end) // 2
    sum_v = sum([a//mid for a in array])
    if sum_v >= target:
        return mid
    if sum_v < target:
        return mid-1
    else:
        return -1


if __name__ == "__main__":
    n, k = map(int, input().split())
    array = [int(input()) for _ in range(n)]
    max_v = max(array)
    print(upper_bound(1, max_v, k))