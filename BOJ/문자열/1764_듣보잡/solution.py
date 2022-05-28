import sys

if __name__ == "__main__":
    n, m = map(int, input().split())
    listeners = dict()
    for _ in range(n):
        listeners[sys.stdin.readline().rstrip()] = 0
    for _ in range(m):
        looker = sys.stdin.readline().rstrip()
        if looker in listeners.keys():
            listeners[looker] = 1
    print(sum(listeners.values()))
    keys = sorted(list(listeners.keys()))
    for key in keys:
        if listeners[key] == 1:
            print(key)

