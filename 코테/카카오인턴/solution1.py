def solution(survey, choices):
    result = ""
    character_dict = {
        "R": 0,
        "T": 0,
        "C": 0,
        "F": 0,
        "J": 0,
        "M": 0,
        "A": 0,
        "N": 0,
    }
    for character, choice in zip(survey, choices):
        if choice <= 3:
            character_dict[character[0]] += abs(choice-4)
        elif choice >= 5:
            character_dict[character[1]] += abs(choice-4)

    keys = list(character_dict.keys())

    for i in range(0,len(keys),2):
        if character_dict[keys[i]] >= character_dict[keys[i+1]]:
            result += keys[i]
        else:
            result += keys[i+1]

    return result



if __name__ == "__main__":
    survey = ["TR", "RT", "TR"]
    choices = [4,4,4]
    print(solution(survey, choices))