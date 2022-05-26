# DP로 풀었음


def solution(v):
    if v == 1:
        return 1
    elif v == 2:
        return 2
    elif v == 3:
        return 4
    else:
        return solution(v-1) + solution(v-2) + solution(v-3)


if __name__ == "__main__":
    n = int(input())
    array = [int(input()) for _ in range(n)]

    for v in array:
        print(solution(v))