def solution(n, x):
    x.sort(reverse=True)
    max = 0
    for index, value in enumerate(x):
        tmp = (index+1)*value
        if tmp > max:
            max = tmp
    return max


if __name__ == "__main__":
    n = int(input())
    x = [int(input()) for _ in range(n)]
    print(solution(n, x))
