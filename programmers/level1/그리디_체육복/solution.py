def solution(n, lost, reserve):
    count = 0
    lost, reserve = list(set(lost)-set(reserve)), list(set(reserve)-set(lost))
    for lost_v in lost:
        for reserve_v in reserve:
            if lost_v - 1 == reserve_v or reserve_v == lost_v + 1:
                reserve.remove(reserve_v)
                count += 1
                break

    answer = n - len(lost) + count

    return answer

if __name__ == "__main__":
    n = 5
    lost = [1,2,4]
    reserve = [2,3,4,5]
    print(solution(n,lost,reserve))