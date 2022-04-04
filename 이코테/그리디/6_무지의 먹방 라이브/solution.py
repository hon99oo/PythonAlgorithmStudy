def solution(food_times, k):
    length = len(food_times)
    quotient = k // length
    remainder = k % length
    food_times = [v-quotient-1 if i<remainder else v-quotient for i,v in enumerate(food_times)]
    time_sum = sum([i for i in food_times if i<0])
    index = (remainder + time_sum) % length
    if food_times[index] <= 0:
        for i,v in enumerate(food_times[index:]):
            if v > 0:
                return i+index+1
        return -1
    return index


def solution2(food_times, k):
    length = len(food_times)
    index = -1
    while k > 0:
        index += 1
        if food_times[index % length] == 0:
            continue
        else:
            food_times[index % length] -= 1
            k -= 1

    index = (index + 1) % length

    if food_times[index] <= 0:
        for i in range(length+1):
            if food_times[(index+i) % length] > 0:
                return (index+i) % length + 1
        return -1

    return index+1


def solution3(food_times, k):
    import heapq

    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0
    previous = 0

    length = len(food_times)
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key =lambda x: x[1])
    return result[(k - sum_value) % length][1]


if __name__ == "__main__":
    food_times = [3,1,1,1,2,4,3]
    k = 12
    print(solution3(food_times,k))