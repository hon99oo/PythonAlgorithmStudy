def solution(array,n):
    array.sort()
    sum_v = 0
    for i in range(n):
        sum_v += sum(array[:i+1])

    return sum_v


if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))
    print(solution(array,n))