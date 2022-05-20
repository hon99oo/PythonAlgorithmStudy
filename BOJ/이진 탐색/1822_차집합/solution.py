if __name__ == "__main__":
    n, m = map(int, input().split())
    n_set = set(map(int, input().split()))
    m_set = set(map(int, input().split()))
    answer = list(n_set-m_set)
    answer.sort()
    length = len(answer)
    print(length)
    if length > 0:
        print(*answer)
