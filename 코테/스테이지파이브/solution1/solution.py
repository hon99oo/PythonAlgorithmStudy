def solution(n):
    store = 0
    digit = 1
    nine = 9

    while n > digit * nine:
        n -= (digit * nine)
        store += nine
        digit += 1
        nine *= 10

    answer = (store + 1) + ((n - 1) // digit)

    return int(str(answer)[(n - 1) % digit])

if __name__ == "__main__":
    n = 1000000000
    print(solution(n))