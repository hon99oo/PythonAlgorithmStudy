def solution(tstring, variables):
    # 단어 단위로 탐색하기 위해 string to list
    tlist = tstring.split(' ')

    # '변수'를 key 값으로, '값'을 value 값으로 dictionary 정의
    dic = {v[0]: v[1] for v in variables}

    # tlist 탐색하며 템플릿 문자열 변경(변경된 값이 처음값이라면 무한히 반복하는 것으로 판단, dic에 저장되어 있지 않은 템플릿은 예외처리)
    for i in range(len(tlist)):
        first = tlist[i]
        while True:
            if tlist[i][0] == "{":
                try:
                    tlist[i] = dic[tlist[i][1:-1]]
                except:
                    break
                if tlist[i] == first:
                    break
            else:
                break

    # 기존의 string 타입으로 변경
    answer = ' '.join(tlist)

    return answer

if __name__ == "__main__":
    tstring = "{a} {b} {c} {d} {i}"
    variables = [["b", "{c}"], ["a", "{b}"], ["e", "{f}"], ["h", "i"], ["d", "{e}"], ["f", "{d}"], ["c", "d"]]
    print(solution(tstring, variables))