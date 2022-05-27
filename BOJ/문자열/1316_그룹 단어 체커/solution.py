import sys


def solution(string):
    length = len(string)
    for i in range(length):
        flag = False
        for j in range(i+1, length):
            if string[i] != string[j]:
                flag = True
            if string[i] == string[j] and flag:
                return False
    return True


if __name__ == "__main__":
    n = int(input())
    strings = [sys.stdin.readline().rstrip() for _ in range(n)]
    count = 0
    for string in strings:
        if solution(string):
            count += 1
    print(count)
