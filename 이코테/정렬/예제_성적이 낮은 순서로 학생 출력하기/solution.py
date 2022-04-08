def solution(array):
    array.sort(key= lambda x: x[1])


if __name__ == "__main__":
    array = [
        ["홍길동", 95],
        ["이순신", 77]
    ]
    solution(array)
    print(array)