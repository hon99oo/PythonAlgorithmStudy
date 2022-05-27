def solution(array, n):
    answer = [0,array[0]]
    for i in range(1,n):
        answer.append(answer[i] + array[i])
    for action in actions:
        print(answer[action[1]] - answer[action[0]-1])


if __name__ == "__main__":
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    actions = [list(map(int, input().split())) for _ in range(m)]
    solution(array, n)