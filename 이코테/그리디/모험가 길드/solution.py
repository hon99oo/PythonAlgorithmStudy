def solution(array):
    count = 0
    array.sort(reverse=True)
    while array:
        array = array[array[0]:]
        count += 1

    return count

if __name__ == "__main__":
    array = [2,3,1,2,2]
    print(solution(array))