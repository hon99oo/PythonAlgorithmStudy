def solution(str):
    if str[-1] == '1':
        str += '0'
    else:
        str += '1'
    count_0 = 0
    count_1 = 0

    for i in range(len(str)-1):
        if str[i]+str[i+1] == '01':
            count_0 += 1
        if str[i]+str[i+1] == '10':
            count_1 +=1

    return min(count_0,count_1)



if __name__ == "__main__":
    str = "010"
    print(solution(str))