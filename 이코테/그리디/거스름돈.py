def solution(money):
    answer = 0
    answer += money//500
    money = money%500
    answer += money//100
    money = money%100
    answer += money//50
    money = money%50
    answer += money//10

    return answer

def solution2(money):
    coin_types = [500, 100, 50, 10]
    count = 0

    for coin in coin_types:
        count += money // coin
        money %= coin

    return count

if __name__ == "__main__":
    money = 1260
    print(solution2(money))