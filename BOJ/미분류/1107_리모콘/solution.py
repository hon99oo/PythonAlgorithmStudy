def solution(broken, k):
    min_v = abs(100 - k)
    for num in range(1000001):
        for N in str(num):
            if N in broken:
                break
        else:
            min_v = min(min_v, len(str(num)) + abs(num - k))

    return min_v


if __name__ == "__main__":
    k = int(input())
    m = int(input())
    if m:
        broken = set(input().split())
    else:
        broken = set()
    print(solution(broken,k))
