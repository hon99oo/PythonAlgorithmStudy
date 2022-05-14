def solution(k):
    degree = 0
    while True:
        if 2**degree >= k:
            break
        degree += 1

    size = 2**degree
    if k == size/2:
        return 1
    if k%2 == 1:
         return size, degree
    for s in reversed(range(degree+1)):
        if k%(2**s) == 0:
            return size, degree - s


if __name__ == "__main__":
    k = int(input())
    m, n = solution(k)
    print(m, n)