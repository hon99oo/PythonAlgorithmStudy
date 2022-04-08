# 순차 탐색 소스코드 구현
def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인하며
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일할 경우
        if array[i] == target:
            return i + 1 # 현재의 위치 반환(인덱스는 0부터 시작하므로 1 더하기)


if __name__ == "__main__":
    n = 5
    target = "apple"
    array = ["banana", "mango", "melon", "apple", "kakao"]
    print(sequential_search(n, target, array))