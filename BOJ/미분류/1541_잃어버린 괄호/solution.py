import sys


def solution(string):
    index = 0
    array = []
    for i, s in enumerate(string):
        if s == '-':
            array.append([index, i])
            index = i+1
    array.append([index, len(string)])

    store = []
    for a in array:
        num = ''
        tmp = 0
        for i in range(a[0], a[1]):
            if string[i] == '+':
                tmp += int(num)
                num = ''
            else:
                num += string[i]
        if tmp == 0:
            tmp = int(num)
        else:
            tmp += int(num)
        store.append(tmp)
    answer = store[0] - sum(store[1:])
    return answer


if __name__ == "__main__":
    string = sys.stdin.readline().rstrip()
    print(solution(string))
