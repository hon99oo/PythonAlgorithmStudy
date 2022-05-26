def solution(call):
    # 대소문자 구분 없이 체크하기 위해 소문자로 통일
    lower_call = call.lower()

    # 알파벳 하나 기준 문자열에 몇개 있는지 체크
    call_list = list(set(lower_call))
    count_list = []
    for c in call_list:
        count_list.append((c,lower_call.count(c)))

    # 가장 많이 존재하는 문자 모두 remove_set에 저장
    count_list.sort(key=lambda x: x[1], reverse=True)
    remove_set = set()
    for s in count_list:
        if s[1] == count_list[0][1]:
            remove_set.add(s[0])

    # remove_set에 포함된 알파벳(대소문자) 제거
    answer = ''.join([i for i in call if not i.lower() in remove_set])
    return answer


if __name__ == "__main__":
    call = "AAAAAABb"
    print(solution(call))