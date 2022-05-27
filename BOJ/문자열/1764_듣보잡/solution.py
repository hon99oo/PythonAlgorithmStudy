import sys


if __name__ == "__main__":
    n, m = map(int, input().split())
    listeners = [sys.stdin.readline().rstrip() for _ in range(n)]
    lookers = [sys.stdin.readline().rstrip() for _ in range(m)]
    print(listeners)
    print("!!")
    print(lookers)