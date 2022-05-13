def solution(n, students):
    students.sort()
    result = min([students[i]+students[(n*2)-1-i] for i in range(n)])
    return result


if __name__ == "__main__":
    n = int(input())
    students = list(map(int, input().split()))
    print(solution(n, students))