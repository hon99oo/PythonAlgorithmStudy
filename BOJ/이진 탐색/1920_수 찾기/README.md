# BOJ

## 이진 탐색 1920 수 찾기
[문제로 이동!](https://www.acmicpc.net/problem/1920)

## 문제

N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

## 입력

첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

## 예제 입력
{% highlight python %}

    """
    case 1:
    입력
    5
    4 1 5 2 3
    5
    1 3 7 9 5
    출력
    1
    1
    0
    0
    1

    case 2:
    입력
    4                      
    2147483647 10 -2147483640 0
    6
    0 -2147483640 10000000 0 2147483647 9 
    출력
    1
    1
    0
    1
    1
    0
    """
{% endhighlight %}

## 풀이
> 이진 탐색을 통해서 풀었다. 하지만 target의 값이 num_list의 범위 밖으로 벗어난다면, 예외처리를 해준다.

## 코드

{% highlight python %}

    def binary_search(num_list, target, start, end):
        while start <= end:
            mid = (start + end) // 2
            if num_list[mid] == target:
                return 1
            elif num_list[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return 0
    
    
    def solution(n, num_list, find_list):
        num_list.sort()
        result = []
        max_v = max(num_list)
        min_v = min(num_list)
        for f in find_list:
            if min_v <= f <= max_v:
                result.append(binary_search(num_list, f, 0, n))
            else:
                result.append(0)
        return result
    
    
    if __name__ == "__main__":
        n = int(input())
        num_list = list(map(int, input().split()))
        m = int(input())
        find_list = list(map(int, input().split()))
        answer = solution(n, num_list, find_list)
        for v in answer:
            print(v)
{% endhighlight %}