def solution(array, n, s):
    start = 0
    end = 0
    min_v = len(array)+1
    store = 0
    sum_v = array[0]
    flag = 0
    while True:
        # print(start, end, sum_v)
        if end > n-1 or start > n-1:
            break
        if sum_v >= s:
            store = end-start+1
            # print("!!", start, end, sum_v, store)
            if store < min_v:
                min_v = store
                flag = 1
                # print(f"index = {start}-{end}, array = {array[start:end+1]}, sum = {sum_v}, min_v = {min_v}")
        if sum_v >= s:
            sum_v -= array[start]
            start += 1
        elif sum_v < s:
            end += 1
            if end < n:
                sum_v += array[end]
    if flag == 0:
        return 0
    else:
        return min_v


if __name__ == "__main__":
    n, s = map(int, input().split())
    array = list(map(int, input().split()))
    print(solution(array, n, s))