def solution(n, a, b):
    a.sort(reverse=True)
    b.sort()
    return sum([x*y for x, y in zip(a, b)])


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solution(n, a, b))