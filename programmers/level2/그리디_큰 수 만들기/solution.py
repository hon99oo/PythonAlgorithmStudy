def solution1(number, k):
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

def solution2(number, k):
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



def solution3(number,k):
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
    print(solution3(number, k))