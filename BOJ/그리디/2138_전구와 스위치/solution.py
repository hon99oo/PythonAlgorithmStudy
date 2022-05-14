import sys


def change(first, i, n):
    if i != 0:
        if first[i - 1] == "0":
            first[i - 1] = "1"
        else:
            first[i - 1] = "0"
    if first[i] == "0":
        first[i] = "1"
    else:
        first[i] = "0"
    if i != n - 1:
        if first[i + 1] == "0":
            first[i + 1] = "1"
        else:
            first[i + 1] = "0"


def solution(n, first, last):
    if first == last:
        return 0

    first_f = list(first)
    first_n = list(first)
    last = list(last)
    count_f, count_n = -1, -1

    # 첫 번째 전구를 누르는 경우
    change(first_f, 0, n)
    count = 0
    for i in range(1,n):
        if first_f[i-1] != last[i-1]:
            change(first_f, i, n)
            count += 1
    if first_f == last:
        count_f = count+1

    # 첫 번째 전구를 누르지 않을 경우
    count = 0
    for i in range(1,n):
        if first_n[i-1] != last[i-1]:
            change(first_n, i, n)
            count += 1
    if first_n == last:
        count_n = count

    if count_n == -1 and count_f != -1:
        return count_f
    elif count_n != -1 and count_f == -1:
        return count_n
    elif count_n != -1 and count_f != -1:
        return min(count_f, count_n)
    else:
        return -1


if __name__ == "__main__":
    n = int(input())
    first = sys.stdin.readline().rstrip()
    last = sys.stdin.readline().rstrip()
    print(solution(n, first, last))