from itertools import combinations


def solution(array, L, bf, enemy):
    skill_sum = sum(array) # 총합
    array = [(v, index) for index, v in enumerate(array)] # 튜플
    best = array[bf-1] # 절친 튜플
    array.pop(enemy-1) # 원수 pop
    youngseo = array.pop(0) # 본인 pop
    comb = list(combinations(array, 10)) # combination

    win_match = 0
    all_match = 0

    for c in comb:
        a_sum = youngseo[0]
        for v in c:
            a_sum += v[0]
        b_sum = skill_sum - a_sum
        if best in c:
            a_sum += 5
        difference = a_sum - b_sum
        if abs(difference) >= L:
            continue
        elif difference >= L/2:
            win_match += 4
        elif difference >= L/4:
            win_match += 3
        elif difference > -L/4:
            win_match += 2
        elif difference > -L/2:
            win_match += 1
        elif difference <= -L/2:
            win_match += 0
        all_match += 4

    if all_match == 0:
        return "No match available"
    else:
        return round((win_match/all_match)*100, 2)


if __name__ == "__main__":
    T = int(input())
    result = []
    for i in range(T):
        L = int(input())
        array = list(map(int,input().split()))
        bf, enemy = map(int, input().split())
        result.append(solution(array, L, bf, enemy))
    for i, r in enumerate(result):
        if type(r) == float:
            print("#{} {:.2f}%".format(i+1,r))
        else:
            print("#{} {}".format(i+1, r))

