def upper_bound(array, target, start, end):
    while start < end:
        mid = (start + end) // 2
        if array[mid] <= target:
            start = mid + 1
        elif array[mid] > target:
            end = mid
    mid = (start + end) // 2
    if array[mid] > target:
        return mid
    else:
        return -1


if __name__ == "__main__":
    target = 4
    array = [1,2,4,4,4,4,4,4,4]
    print(upper_bound(array, target, 0, len(array)-1))