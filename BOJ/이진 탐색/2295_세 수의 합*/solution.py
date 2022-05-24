def solution(array, n):
    array.sort()
    sum_set = set()
    for i in range(n):
        for j in range(n):
            sum_set.add(array[i] + array[j])

    answer = []
    for i in range(n-1, -1, -1):
        for j in range(i+1):
            if array[i] - array[j] in sum_set:
                answer.append(array[i])
                break
    answer.sort()
    return answer[-1]

if __name__ == "__main__":
    n = int(input())
    array = []
    for _ in range(n):
        array.append(int(input()))

    print(solution(array, n))