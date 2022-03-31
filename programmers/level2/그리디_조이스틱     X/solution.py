def solution(name):
    name, base = list(name), list("A"*len(name))
    up = [ord(_name)-ord(_base) for _name,_base in zip(name,base)]
    down = [abs(ord(_name)-ord(_base)-26) for _name,_base in zip(name,base)]
    up_and_down = [min(_up,_down) for _up,_down in zip(up,down)]
    answer = sum(up_and_down) + len(up_and_down) - 1

    return(answer)


if __name__ == "__main__":
    name = "BBBABAABABA"
    print(solution(name))
