def binary_search(array, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        value = array[0]
        count = 1
        for i in range(1,n):
            if array[i] >= value +mid:
                value = array[i]
                count +=1
        if count >= c:
            start = mid + 1
            result = mid
        else:
            end = mid - 1

    return result


if __name__ == "__main__":
    n, c = map(int, input().split())
    array = []
    for _ in range(n):
        array.append(int(input()))
    array.sort()
    end = array[-1] - array[0]
    print(binary_search(array, 1, end))