def upper_bound(start, end, target):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        sum_v = sum(map(lambda x: x//mid, array))
        if sum_v >= target:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
    return result


if __name__ == "__main__":
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    if sum(array) < n:
        print(0)
    else:
        print(upper_bound(1,max(array),n))