def solution(n, m, course):
    mileage = []
    for i in range(n):
        if course[i][1] - course[i][0] > 0:
            mileage.append(1)
        else:
            course[i][2].sort()
            mileage.append(course[i][2][course[i][0] - course[i][1]])

    mileage.sort()
    sum_v = 0
    count = 0
    for v in mileage:
        if v > 36:
            continue
        sum_v += v
        if sum_v > m:
            return count
        count += 1

    return count


if __name__ == "__main__":
    n, m = map(int, input().split())
    course = []
    for _ in range(n):
        register, possible = map(int, input().split())
        course.append((register, possible, list(map(int, input().split()))))
    print(solution(n, m, course))