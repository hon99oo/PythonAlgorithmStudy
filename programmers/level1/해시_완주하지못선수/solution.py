def solution1(participant,completion):
    answer = []
    participant_dict = {p:participant.count(p) for p in participant}
    for c in completion:
        participant_dict[c] -= 1
    for key in participant_dict.keys():
        if participant_dict[key] > 0:
            return answer


def solution2(participant,completion):
    participant_dict = {}
    for p in participant:
        if p in participant_dict.keys():
            participant_dict[p] += 1
        else:
            participant_dict[p] = 1
    for c in completion:
        participant_dict[c] -= 1
    for key in participant_dict.keys():
        if participant_dict[key] > 0:
            return key


def solution3(participant,completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer


def solution4(participant, completion):
    import collections
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


if __name__ == "__main__":
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    print(solution2(participant,completion))


