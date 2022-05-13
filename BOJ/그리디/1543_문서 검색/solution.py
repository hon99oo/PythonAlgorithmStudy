import sys

def solution(data, find):
    return data.count(find)


if __name__ == "__main__":
    data = sys.stdin.readline().rstrip()
    find = sys.stdin.readline().rstrip()
    print(solution(data, find))