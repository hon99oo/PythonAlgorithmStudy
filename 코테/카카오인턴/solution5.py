def solution(rc, operations):
    for operation in operations:
        if operation == "Rotate":
            tmp = rc[0][0]
            for i in range(4):
                rc = [list(v) for v in zip(*rc[::-1])]
                rc[0][1:] = rc[0][:-1]
            rc[0][1] = tmp
        if operation == "ShiftRow":
            tmp = rc[len(rc)-1]
            for i in range(len(rc)-1,0,-1):
                rc[i] = rc[i-1]
            rc[0] = tmp
    return rc


if __name__ == "__main__":
    rc = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    operations = ["Rotate"]
    print(solution(rc, operations))