def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0


def solution(n, num_list, find_list):
    answer = []
    num_list.sort()
    for f in find_list:
        answer.append(binary_search(num_list, f, 0, n-1))
    return answer

if __name__ == "__main__":
    n = int(input())
    num_list = list(map(int, input().split()))
    m = int(input())
    find_list = list(map(int, input().split()))
    print(*solution(n, num_list, find_list))
