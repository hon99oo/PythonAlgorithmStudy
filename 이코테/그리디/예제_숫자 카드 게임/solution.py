def solution(array):
    min_n = min(array[0])
    for arr in array:
        if min_n < min(arr):
            min_n = min(arr)

    return min_n

if __name__ == "__main__":
    array = [[7,3,1,8],[3,3,3,4]]
    print(solution(array))