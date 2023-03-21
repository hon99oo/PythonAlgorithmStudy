def solution(n, x):
    x.sort()
    x.sort(key=lambda x: x[1])
    offset = x[0][1]
    cnt = 1
    for v in x[1:]:
        if v[0] >= offset:
            offset = v[1]
            cnt+=1
    return cnt


if __name__ == "__main__":
    n = int(input())
    x = [tuple(map(int, input().split())) for _ in range(n)]
    print(solution(n, x))