def solution(x,y,w,s):
    if s <= w:
        min_val = min(x, y)
        if abs(x-y) % 2 == 0:
            result = ((min_val) * s) + (abs(x-y) * s)
        else:
            result = ((min_val) * s) + ((abs(x-y)-1) * s) + w
    elif s > w*2:
        result = (x+y) * w
    else:
        min_val = min(x,y)
        result = ((min_val) * s) + (abs(x-y) * w)

    return result


if __name__ == "__main__":
    x, y, w, s = map(int, input().split())
    print(solution(x,y,w,s))