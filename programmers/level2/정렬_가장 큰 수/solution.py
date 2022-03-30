def solution(numbers):
    if sum(numbers)==0:
        return '0'
    numbers = sorted([str(number)*3 for number in numbers],reverse=True)
    answer = ''.join([numbers[i][:int(len(numbers[i])/4)] for i in range(len(numbers))])
    return answer

if __name__ == "__main__":
    numbers = [6,2,10]
    print(solution(numbers))