from math import factorial


def solution(n):
    value = str(factorial(n))
    length = len(value)
    count = 0
    print(value)
    for i in range(length-1, -1, -1):
        print(value[i])
        if value[i] != '0':
            break
        count += 1
    return count


if __name__ == "__main__":
    n = int(input())
    print(solution(n))