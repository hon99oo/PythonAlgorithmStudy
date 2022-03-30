import time

def solution(number, k):
    number = list(number)
    length = len(number)-k
    count = 0
    tmp = 0
    for _ in range(k):
        for i in range(0,len(number)-1):
            i = i + tmp
            if number[i] < number[i+1]:
                number.pop(i)
                count += 1
                break
    number = number[:length]
    answer = ''.join(number)
    return answer

def solution2(number, k):
    number = list(number)
    i = 0;
    while k > 0:
        for j in range(i,i+k+1):
            if number[i] == '9': break
            if number[i] < number[j]:
                number.pop(i)
                k = k -1
                if i>0:
                    i = i -1
                    break
                i = -1
                break
        i += 1
    answer = ''.join(number)
    return answer

def solution3(number, k):
    number = list(number)
    length = len(number)-k
    answer = []
    for _ in range(length):
        answer.append(max(number[:k+1]))




if __name__ == "__main__":
    number = '999988887777666655554444333322221111123456789'
    k = 43
    start = time.time()
    print(solution(number, k))
    print(time.time()-start)