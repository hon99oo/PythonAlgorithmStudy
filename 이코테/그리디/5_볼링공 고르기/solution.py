def solution(array):
    count = 0
    array.sort()
    for i,i_val in enumerate(array):
        for j_val in array[i+1:]:
            if i_val != j_val:
                count += 1
    return count


def solution2(array):
    n = len(array)
    weight_list = [0] * 11

    for x in array:
        weight_list[x] += 1

    result = 0
    for i in range(1, max(array)+1):
        n -= weight_list[i]
        result += weight_list[i] * n

    return result


if __name__ == "__main__":
    array = [1,3,2,3,2]
    print(solution2(array))