def solution(str):
    sum = int(str[0])

    for ch in str[1:]:
        ch = int(ch)
        if sum < 2 or ch < 2:
            sum += ch
        else:
            sum *= ch

    return sum


if __name__ == "__main__":
    str = "567"
    print(solution(str))