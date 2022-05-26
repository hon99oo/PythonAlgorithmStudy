def two_pointer(array, basis, start, end):
    global value
    global answer
    while start < end:
        x = array[basis] + array[start] + array[end]
        if abs(value) > abs(x):
            value = x
            answer = [array[basis],array[start],array[end]]
        if x < 0:
            start += 1
        elif x > 0:
            end -= 1
        else:
            answer = [array[basis],array[start],array[end]]
            return True
    return False


if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))
    array.sort()
    value = array[0] + array[1] + array[2]
    answer = [array[0],array[1],array[2]]
    for i in range(n):
        if two_pointer(array, i, i+1, n-1):
            break
    print(*answer)