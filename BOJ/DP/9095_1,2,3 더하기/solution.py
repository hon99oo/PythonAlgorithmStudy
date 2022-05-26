# 백트래킹으로 풀었음


import sys
sys.setrecursionlimit(10**6)


def dfs(x, case, numbers):
    global count
    global answer

    sum_v = sum(case)
    if sum_v == x:
        if not case in answer:
            count += 1
            answer.append(case.copy())
        case.pop()
        return
    elif sum_v > x:
        case.pop()
        return
    else:
        for number in numbers:
            case.append(number)
            dfs(x, case, numbers)

    if len(case) > 0:
        case.pop()

    return

if __name__ == "__main__":
    n = int(input())
    array = [int(input()) for _ in range(n)]
    numbers = [1,2,3]
    case = []
    count = 0
    flag = False
    answer = []
    for x in array:
        dfs(x, case, numbers)
        print(count)
        count = 0