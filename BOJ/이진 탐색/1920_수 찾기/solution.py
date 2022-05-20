def binary_search(num_list, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if num_list[mid] == target:
            return 1
        elif num_list[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0


def solution(n, num_list, find_list):
    num_list.sort()
    result = []
    max_v = max(num_list)
    min_v = min(num_list)
    for f in find_list:
        if min_v <= f <= max_v:
            result.append(binary_search(num_list, f, 0, n))
        else:
            result.append(0)
    return result


if __name__ == "__main__":
    n = int(input())
    num_list = list(map(int, input().split()))
    m = int(input())
    find_list = list(map(int, input().split()))
    answer = solution(n, num_list, find_list)
    for v in answer:
        print(v)
