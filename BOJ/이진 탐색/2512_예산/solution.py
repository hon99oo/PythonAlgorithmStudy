def upper_bound(start, end, target):
    while start < end:
        mid = (start + end) // 2
        sum_v = sum(map(lambda i: min(i, mid), array))
        if sum_v <= target:
            start = mid + 1
        else:
            end = mid
    mid = (start + end) // 2
    return mid - 1


if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))
    m = int(input())
    total = sum(array)
    if total <= m:
        print(max(array))
    else:
        print(upper_bound(1, m, m))