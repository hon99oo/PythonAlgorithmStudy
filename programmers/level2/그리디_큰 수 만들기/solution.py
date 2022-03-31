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
    remove_list = []
    i = 0
    while k > 0:
        if i+1+k > len(number):
            break
        for j in range(i+1,i+1+k):
            if number[i] < number[j]:
                remove_list.append(i)
                k -= 1
                break
        i += 1
    number = [number[i] for i in range(len(number)) if i not in remove_list]
    number = number[:length]
    answer = ''.join(number)
    return answer


def solution4(number, k):
    number = list(number)
    length = len(number)-k
    remove_list = []
    i = 0
    count = 0
    flag = 0
    while k > 0:
        if i+1+k > len(number):
            break
        for j in range(i+1,i+1+k):
            if number[i] > number[j]:
                remove_list.append[j]
                count+=1
            elif number[i] == number[j]:
                k -= count
                i += count
            elif number[i] < number[j]:
                remove_list.append[i]
                k -= count
                i += count
                count = 0
                flag = 1
                break
        if flag == 0:
            break


def solution5(number, k):
    length = len(number) - k
    answer = []
    end = len(number) - (length-1)
    while len(answer) != length:
        temp = "0"
        for i in range(len(number[0:end])):
            if number[i] > temp:
                temp = number[i]
                p = i
                if number[i] == "9":
                    break
        if temp == "0":
            p = 0
        answer.append(temp)
        number = number[p+1:]
        end = len(number) - (length - 1 -len(answer))

    answer = ''.join(answer)
    return answer

def solution6(number,k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)

if __name__ == "__main__":
    number = '4177252841'
    k = 4
    print(solution6(number, k))