import time
import sys
sys.setrecursionlimit(100000)

def solution(string):
    total_list = []
    num_sum = 0
    for i,v in enumerate(string):
        if v == "W":
            total_list.append(["W"])
        if v == "H":
            for l in total_list:
                if l[-1] == "W":
                    l.append(v)
            total_list.append(["W"])
        if v == "E":
            for l in total_list:
                if l[-1] == "H":
                    l.append(0)
                if type(l[-1]) == int:
                    l[-1] += 1

    total_list = [i for i in total_list if type(i[-1]) == int]

    for l in total_list:
        n = l[-1]
        if n >= 2:
            num_sum += 2**n - n - 1

    return num_sum


def combination_sum(n):
    num_sum = 0
    for i in range(2,n+1):
        num_sum += combination(n, i)
    return num_sum


def combination(n, k):
    if n == k: return 1
    elif k == 1: return n
    else: return combination(n-1,k-1) + combination(n-1,k)


if __name__ == "__main__":
    string = "WHEEWHEEWHEEWHEEWHEE" * 500

    # start = time.time()
    # print(solution(string))
    # print(time.time()-start)

    def countingE(N):
        return 2 ** N - 1 - N


    answer = 0


    S = string
    start = time.time()
    for index1 in range(len(S) - 3):
        if S[index1] == 'W':
            for index2 in range(index1, len(S) - 2):
                if S[index2] == 'H':
                    tmp = S[index2:]
                    tmpCountE = tmp.count('E')
                    if tmpCountE >= 2:
                        answer += countingE(tmpCountE)
    print(time.time()-start)