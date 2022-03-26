def solution(numbers):
    prime_list = create_prime_list(numbers)
    answer = check_num(numbers, prime_list)
    return answer


def create_prime_list(numbers):
    prime_list = []
    for i in range(2, int(''.join(sorted(numbers, reverse=True)))):
        if is_prime_num(i):
            prime_list.append(i)
    return prime_list


def is_prime_num(n):
    n = int(n)
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def check_num(numbers, prime_list):
    answer = 0
    for prime in prime_list:
        count = 0
        for n in list(str(prime)):
            if n in numbers:
                count+=1
        if count == len(str(prime)):
              answer += 1
    return answer

if __name__ == "__main__":
    numbers = "011"
    print(solution(numbers))
