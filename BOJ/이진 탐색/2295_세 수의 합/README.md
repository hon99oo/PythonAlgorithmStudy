# BOJ

## 이진 탐색 2110 공유기 설치
[문제로 이동!](https://www.acmicpc.net/problem/2110)

## 문제

N(5 ≤ N ≤ 1,000)개의 자연수들로 이루어진 집합 U가 있다. 이 중에서 적당히 세 수를 골랐을 때, 그 세 수의 합 d도 U안에 포함되는 경우가 있을 수 있다. 이러한 경우들 중에서, 가장 큰 d를 찾으라.

예를 들어 {2, 3, 5, 10, 18}와 같은 집합이 있다고 하자. 2+3+5 = 10이 되고, 이 수는 집합에 포함된다. 하지만 3+5+10 = 18이 되고, 이 경우가 세 수의 합이 가장 커지는 경우이다.

## 입력

첫째 줄에 자연수 N이 주어진다. 다음 N개의 줄에 차례로 U의 원소가 하나씩 주어진다. 주어진 U는 집합이 되므로 입력되는 두 수가 같아서는 안 된다. U의 원소는 200,000,000보다 작거나 같은 자연수이다. 답이 항상 존재하는 경우만 입력으로 주어진다.

## 예제 입력
{% highlight python %}

    """
    case 1:
    입력
    5
    2
    3
    5
    10
    18
    출력
    18
    """
{% endhighlight %}

## 풀이
> x+y+z=k를 반복문을 돌며 탐색한다면 N^3의 시간이 소요된다. 하지만 x+y=k-z 로 식을 치환해서 반복문을 돈다면 N^2의 시간이 소요되므로 더 빠른 속도로 문제를 해결할 수 있다.
> 또한 x+y를 set 자료구조에 추가하여 중복을 자동으로 제거한다.

## 코드

{% highlight python %}

    def solution(array, n):
        array.sort()
        sum_set = set()
        for i in range(n):
            for j in range(n):
                sum_set.add(array[i] + array[j])
    
        answer = []
        for i in range(n-1, -1, -1):
            for j in range(i+1):
                if array[i] - array[j] in sum_set:
                    answer.append(array[i])
                    break
        answer.sort()
        return answer[-1]
    
    if __name__ == "__main__":
        n = int(input())
        array = []
        for _ in range(n):
            array.append(int(input()))
    
        print(solution(array, n))
{% endhighlight %}