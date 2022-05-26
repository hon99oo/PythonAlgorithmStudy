from collections import deque
def solution(queue1, queue2):
    count = 0

    deq1 = deque(queue1)
    deq2 = deque(queue2)

    sum1 = sum(deq1)
    sum2 = sum(deq2)

    if (sum1+sum2)%2 == 1:
        return -1

    deq1_set = set()
    deq2_set = set()

    while(sum1 != sum2):
        deq1_set.add(str(deq1))
        deq2_set.add(str(deq2))
        if sum1 > sum2:
            val = deq1.popleft()
            deq2.append(val)
            sum1 -= val
            sum2 += val
        elif sum1 < sum2:
            val = deq2.popleft()
            deq1.append(val)
            sum1 += val
            sum2 -= val
        else:
            return count
        count += 1
        if str(deq1) in deq1_set or str(deq2) in deq2_set:
            return -1

    return count

if __name__ == "__main__":
    queue1 = [2]
    queue2 = [100]*4
    print(solution(queue1, queue2))