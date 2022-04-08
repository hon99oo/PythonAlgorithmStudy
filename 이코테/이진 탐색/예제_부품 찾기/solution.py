def solution(array, target, start, end):
    array.sort()
    result = []
    for t in target:
        while start <= end:
            mid = (start + end) // 2
            if array[mid] == t:
               result.append("Yes")
               break
            elif array[mid] > t:
                end = mid - 1
            else:
                start = mid + 1
        if array[mid] != t:
            result.append("No")
        start = 0
        end = len(array)-1

    return result


def solution2(array, target):
    def binary_search(array, target, start, end):
        while start <= end:
            mid = (start + end) //2
            if array[mid] == target:
                return mid
            elif array[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return None

    store = []

    for i in target:
        result = binary_search(array, i, 0, len(array)-1)
        if result != None:
            store.append("Yes")
        else:
            store.append("No")

    return store


if __name__ == "__main__":
    array = [9, 3, 7, 9, 2]
    target = [5, 7, 9]
    print(solution(array, target, 0, len(array)-1))