def solution(path):
    # direction 정의
    direction = {
        "NE": "right",
        "ES": "right",
        "SW": "right",
        "WN": "right",
        "EN": "left",
        "SE": "left",
        "WS": "left",
        "NW": "left"
    }

    # 방향이 변경되는 지점 저장
    # NNNEEESSSWW
    #    3,E   6,S,  9,W
    direction_change_list = []
    for i in range(len(path)-1):
        if path[i] != path[i+1]:
            direction_change_list.append((i+1,path[i]+path[i+1]))

    # 첫번째 메세지
    time = 0
    distance = direction_change_list[0][0]
    if distance > 5:
        time = distance - 5
        distance = 5
    message = f"Time {time}: Go straight {distance*100}m and turn {direction[direction_change_list[0][1]]}"

    result = []
    result.append(message)

    # 두번째 메세지 ~ 마지막 메세지
    for i in range(len(direction_change_list)-1):
        time = direction_change_list[i][0]
        distance = (direction_change_list[i+1][0]-direction_change_list[i][0])
        if distance > 5:
            time = direction_change_list[i][0] + distance - 5
            distance = 5
        message = f"Time {time}: Go straight {distance*100}m and turn {direction[direction_change_list[i+1][1]]}"
        result.append(message)

    return result



if __name__ == "__main__":
    path = "NNNNEEEEEEEES"
    print(solution(path))