def solution(M, K, array):
    answer = 0
    array.sort(reverse=True)
    for i in range(1,M+1):
        if i%(K+1) == 0:
            answer += array[1]
        else:
            answer += array[0]

    return answer

def solution2(M, K, array):
    array.sort()
    first = array[-1]
    second = array[-2]

    count = (int(M/(K+1)) * K) + (M % (K+1))

    result = 0
    result += (count) * first
    result += (M - count) * second

    return result

if __name__ == "__main__":
    M = 7
    K = 2
    array = [3,4,3,4,3]
    print(solution(M,K,array))