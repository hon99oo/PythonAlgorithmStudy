# BOJ

## 이진 탐색 10815 숫자 카드
[문제로 이동!](https://www.acmicpc.net/problem/10815)

## 문제

숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 두 숫자 카드에 같은 수가 적혀있는 경우는 없다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

## 예제 입력
{% highlight python %}

    """
    case 1:
    입력
    5
    6 3 2 10 -10
    8
    10 9 -5 2 3 4 5 -10
    출력
    1 0 0 1 1 0 0 1
    """
{% endhighlight %}

## 풀이
> 이진 탐색을 사용하면 간단하게 해결할 수 있는 문제다.

## 코드

{% highlight python %}

    def binary_search(array, target, start, end):
        while start <= end:
            mid = (start + end) // 2
            if array[mid] == target:
                return 1
            elif array[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return 0
    
    
    def solution(n, num_list, find_list):
        answer = []
        num_list.sort()
        for f in find_list:
            answer.append(binary_search(num_list, f, 0, n-1))
        return answer
    
    if __name__ == "__main__":
        n = int(input())
        num_list = list(map(int, input().split()))
        m = int(input())
        find_list = list(map(int, input().split()))
        print(*solution(n, num_list, find_list))
{% endhighlight %}