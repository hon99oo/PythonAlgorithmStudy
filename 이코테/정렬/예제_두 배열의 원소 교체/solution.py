def solution(array_A, array_B, k):
    array_A.sort()
    array_B.sort(reverse=True)
    array_B = array_B[:k]
    count = 0

    for i,v in enumerate(array_A):
        if v < min(array_B):
            count += 1
        else:
            break

    min_n = min(count,k)
    return sum(array_A[min_n:]+array_B[:min_n])


def solution2(array_A, array_B, k):
    array_A.sort()
    array_B.sort(reverse=True)

    for i in range(k):
        if array_A[i] < array_B[i]:
            array_A[i] = array_B[i]
        else:
            break

    return sum(array_A)


if __name__ == "__main__":
    k = 3
    array_A = [1, 2, 5, 4, 3]
    array_B = [5, 5, 6, 6, 5]
    print(solution2(array_A, array_B, k))