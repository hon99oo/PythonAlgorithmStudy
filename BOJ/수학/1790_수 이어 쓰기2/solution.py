def solution(k):
    store = 0
    digit = 1
    nine = 9

    while k > digit * nine:
        k -= (digit * nine)
        store += nine
        digit += 1
        nine *= 10

    answer = (store + 1) + ((k - 1) // digit)
    if answer > n:
        return -1
    else:
        return int(str(answer)[(k - 1) % digit])


if __name__ == "__main__":
    n, k = map(int, input().split())
    print(solution(k))