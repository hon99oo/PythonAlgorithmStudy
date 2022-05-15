def solution(numbers):
    numbers.sort()
    result = 0
    negative_list = []
    positive_list = []
    negative_n = 0
    positive_n = 0

    for n in numbers:
        if n <= 0:
            negative_list.append(n)
            negative_n += 1
        else:
            positive_list.append(n)
            positive_n += 1

    if negative_n % 2 == 0:
        for i in range(0,negative_n, 2):
            result += negative_list[i] * negative_list[i+1]
    else:
        for i in range(0, negative_n-1, 2):
            result += negative_list[i] * negative_list[i+1]
        result += negative_list[negative_n-1]

    if positive_n % 2 == 0:
        for i in range(0, positive_n, 2):
            if positive_list[i] > 1 and positive_list[i+1] >1:
                result += positive_list[i] * positive_list[i+1]
            else:
                result += positive_list[i] + positive_list[i+1]
    else:
        for i in range(1, positive_n, 2):
            if positive_list[i] > 1 and positive_list[i+1] >1:
                result += positive_list[i] * positive_list[i+1]
            else:
                result += positive_list[i] + positive_list[i+1]
        result += positive_list[0]


    return result


if __name__ == "__main__":
    n = int(input())
    numbers = []
    for _ in range(n):
        numbers.append(int(input()))
    print(solution(numbers))