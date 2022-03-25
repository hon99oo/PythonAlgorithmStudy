def solution(numbers):
    answer = 0
    if sum(numbers)==0:
        return '0'
    numbers = sorted([str(numbers[i])*3 for i in range(len(numbers))],reverse=True)
    answer = ''.join([numbers[i][:int(len(numbers[i])/4)] for i in range(len(numbers))])
    return answer

if __name__ == "__main__":
    numbers = [6,2,10]
    print(solution(numbers))