def lower_bound(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            if end == mid:
                break
            end = mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    if array[mid] == target:
        return mid
    else:
        return -1


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


def solution(n, num_list, find_list):
    answer = []
    num_list.sort()
    for f in find_list:
        start = lower_bound(num_list, f, 0, n-1)
        if start == -1:
            answer.append(0)
            continue
        end = upper_bound(num_list, f, 0, n-1)
        if end == -1:
            end = n
        count = end - start
        answer.append(count)

    return answer


if __name__ == "__main__":
    n = int(input())
    num_list = list(map(int, input().split()))
    m = int(input())
    find_list = list(map(int, input().split()))
    print(*solution(n, num_list, find_list))

