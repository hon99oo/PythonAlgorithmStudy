import math


def solution(logs):
    logs = list(set(logs))
    log_dict = {}
    name_set = set()
    for log in logs:
        name, problem = log.split(" ")
        name_set.add(name)
        if problem in log_dict:
            log_dict[problem] += 1
        else:
            log_dict[problem] = 1

    answer = []
    length = len(name_set)
    for log in log_dict.keys():
        if log_dict[log] >= math.ceil(length/2):
            answer.append(log)
    answer.sort()
    return answer


if __name__ == "__main__":
    logs = ["kate sqrt"]
    print(solution(logs))