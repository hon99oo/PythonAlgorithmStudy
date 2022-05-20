# lower bound 소스코드 구현(반복문)
def lower_bound(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            if end == mid:
                break
            end = mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    if array[mid] == target:
        return mid
    else:
        return -1

if __name__ == "__main__":
    target = 4
    array = [1,2,4,4,4,4,4,4,4,5]
    print(lower_bound(array, target, 0, len(array)-1))
