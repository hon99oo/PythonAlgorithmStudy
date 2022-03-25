import math

def solution(answers):
    answer = []
    answer_list = [0,0,0]
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if a[i%len(a)]==answers[i]:
            answer_list[0]+=1
        if b[i%len(b)]==answers[i]:
            answer_list[1]+=1
        if c[i%len(c)]==answers[i]:
            answer_list[2]+=1

    for i,val in enumerate(answer_list):
        if val == max(answer_list):
            answer.append(i+1)
    return answer

if __name__ == "__main__":
    answers = [5, 5, 4, 2, 3]
    print(solution(answers))