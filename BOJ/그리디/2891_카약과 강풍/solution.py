def solution(n_list, brk_list, add_list):
    kayak = [1] * n_list[0]
    for i in brk_list:
        kayak[i-1] -= 1
    add_list.sort()
    for i in add_list:
        index = i-1
        kayak[index] += 1
        if kayak[index] >= 2 and index-1 >= 0:
            if kayak[index-1] == 0:
                kayak[index] -= 1
                kayak[index-1] += 1
        if kayak[index] >= 2 and index+1 < n_list[0]:
            if kayak[index+1] == 0:
                kayak[index] -= 1
                kayak[index+1] += 1

    result = kayak.count(0)
    return result


if __name__ == "__main__":
    n_list = list(map(int, input().split()))
    brk_list = list(map(int, input().split()))
    add_list = list(map(int, input().split()))

    print(solution(n_list, brk_list, add_list))