def solution(array, target):
    end = max(array)
    return binary_search(array, target, 0, end)


def binary_search(array, target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        total = sum([0 if i-mid < 0 else i-mid for i in array])
        if total < target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    return result

if __name__ == "__main__":
    target = 6
    array = [19, 15, 10, 17]
    print(solution(array, target))






    n, m = list(map(int, input().split(' ')))
    array = list(map(int, input().split()))