def solution1(array):
    array.sort()
    money_set = set()
    for i in range(len(array)):
        sum = 0
        for j in range(i,len(array)):
            sum += j
            money_set.add(sum)

    for i in range(max(money_set)):
        if i not in money_set:
            return i
    return max(money_set)+1

def solution2(array):
    array.sort()
    target = 1
    for x in array:
        if target < x:
            break
        target += x

    answer = target

    return answer

if __name__ == "__main__":
    array = [3,2,1,1,9]
    print(solution2(array))