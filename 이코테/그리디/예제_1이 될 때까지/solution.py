def solution(n, k):
    count = 0
    while n > 1:
        if n%k==0:
            n = n//k
            count += 1
        else:
            n-=1
            count += 1

    return count


def solution2(n, k):
    result = 0

    while True:
        target = (n // k) * k
        result += (n - target)
        n = target

        if n < k:
            break

        result += 1
        n //= k

    result += (n -1)

    return result


if __name__ == "__main__":
    n = 17
    k = 4
    print(solution(n,k))