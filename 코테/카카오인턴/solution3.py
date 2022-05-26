def solution(alp, cop, problems):
    result = 0
    time = 0
    problems.sort(key = lambda x:max(x[:2]))
    for i in range(len(problems)):
        if [alp,cop] != problems[i][:2]:
            time += (problems[i][0] - alp)
            time += (problems[i][1] - cop)
            alp = problems[i][0]
            cop = problems[i][1]
        min(problems[i+1][:2])


    return result


if __name__ == "__main__":
    alp = 0
    cop = 0
    problems = [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]

    print(solution(alp, cop, problems))