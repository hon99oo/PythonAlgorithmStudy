# 이코테

## 이진탐색 나무 자르기(Python)

## 문제

[문제로 이동!](https://www.acmicpc.net/problem/2805)

## 풀이
> 나무를 자를 수 있는 길이는 0부터 가장 긴 나무의 길이다. 0~가장 긴 나무 길이를 이진 탐색을 하며 잘려진 나무의 합이 목표 길이보다 크다면 자른 길이를 저장한다.
> 최대값을 구하기 위해서 탐색이 종료될 때까지 조건에 맞는 길이를 찾아간다.

1. 나무 길이의 최대 값을 찾는다.
2. start는 0, end는 나무 길이의 최대 값으로 설정한다.
3. 중간 값을 찾고, 나무 길이 - 중간 값을 리스트 컴프리헨션으로 음수가 되는 값은 0으로 변경하여 전체 합을 구한다.
4. 전체합과 target을 비교하여 전체합 보다 target이 작거나 같으면 결과에 중간값을 저장한다.
5. 탐색이 끝날 때 까지 반복하며 최대 값을 구한다.


## 추가 설명
> 해당 문제는 전형적인 이진 탐색 문제이자, 파라메트릭 서치parametric search 유형의 문제라고 한다. "원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제"에 주로 사용한다.
> 예를 들어 범위 내에서 조건을 만족하는 가장 큰 값을 찾으라는 최적화 문제라면 이진 탐색으로 결정 문제를 해결하며 범위를 좁혀갈 수 있다.


## 코드

{% highlight python %}
    
    def solution(array, target):
        end = max(array)
        return binary_search(array, target, 0, end)
    
    
    def binary_search(array, target, start, end):
        result = 0
        while start <= end:
            mid = (start + end) // 2
            total = sum([0 if i-mid < 0 else i-mid for i in array])
            if total < target:
                end = mid - 1
            else:
                result = mid
                start = mid + 1
    
        return result
    
    if __name__ == "__main__":
        target = 6
        array = [19, 15, 10, 17]
        print(solution(array, target))

{% endhighlight %}