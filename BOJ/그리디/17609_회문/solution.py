import sys


def start_pop(string, start, end):
    start += 1
    while start < len(string)//2 + 1:
        if string[start] != string[end]:
            return 2
        start += 1
        end -= 1
    return 1


def end_pop(string, start, end):
    end -= 1
    while start < len(string)//2:
        if string[start] != string[end]:
            return 2
        start += 1
        end -= 1
    return 1


def solution(strings):
    result = []

    for string in strings:
        count = 0
        start = 0
        end = len(string)-1
        while start < len(string)//2:
            if string[start] != string[end]:
                count_sp = start_pop(string, start, end)
                count_ep = end_pop(string, start, end)
                count = min(count_ep, count_sp)
                break
            start += 1
            end -= 1
        result.append(count)
    return result



if __name__ == "__main__":
    n = int(input())
    strings = []
    for _ in range(n):
        strings.append(sys.stdin.readline().rstrip())
    results = solution(strings)
    for result in results:
        print(result)
