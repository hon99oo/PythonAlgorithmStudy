array = [list(map(int, input().split())) for _  in range(int(input()))]
array.sort(key=lambda x: x[1])
array.sort(key=lambda x: x[0])
for a, b in array:
    print(a, b)

