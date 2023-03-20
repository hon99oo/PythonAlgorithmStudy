from collections import deque


def solution(stats):
    queue = deque(stats)
    answer = []
    while queue:
        x = queue.popleft()
        length = len(answer)
        if length < 1:
            answer.append([x])
        else:
            max_index = -1
            for i in range(length):
                if answer[i][-1] < x:
                    max_index = i
                    break
            if max_index == -1:
                answer.append([x])
            else:
                answer[max_index].append(x)

    return len(answer)


if __name__ == "__main__":
    stats = [6, 2, 3, 4, 1, 5]
    print(solution(stats))