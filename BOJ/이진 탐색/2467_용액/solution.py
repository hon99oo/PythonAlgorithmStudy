def binary_search(array, start, end):
    value = array[0] + array[1]
    answer = [array[0], array[1]]
    while start < end:
        x = array[start] + array[end]
        if abs(x) < abs(value):
            value = x
            answer = [array[start], array[end]]
        if x < 0:
            start += 1
        elif x > 0:
            end -= 1
        else:
            break

    return answer


if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))
    start = 0
    end = n-1
    print(*binary_search(array, start, end))