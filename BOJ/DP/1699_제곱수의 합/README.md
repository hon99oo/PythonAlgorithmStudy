# BOJ

## DP 1699 제곱수의 합

[문제로 이동!](https://www.acmicpc.net/problem/2579)

## 문제

어떤 자연수 N은 그보다 작거나 같은 제곱수들의 합으로 나타낼 수 있다. 예를 들어 11=32+12+12(3개 항)이다. 이런 표현방법은 여러 가지가 될 수 있는데, 11의 경우 11=22+22+12+12+12(5개 항)도 가능하다. 이 경우, 수학자 숌크라테스는 “11은 3개 항의 제곱수 합으로 표현할 수 있다.”라고 말한다. 또한 11은 그보다 적은 항의 제곱수 합으로 표현할 수 없으므로, 11을 그 합으로써 표현할 수 있는 제곱수 항의 최소 개수는 3이다.

주어진 자연수 N을 이렇게 제곱수들의 합으로 표현할 때에 그 항의 최소개수를 구하는 프로그램을 작성하시오.


## 입력

첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 100,000)

## 예제 입력
{% highlight python %}

    """
    case 1:
    입력
    7
    출력
    4

    case 2:
    입력
    12
    출력
    3

    case 3:
    입력
    41
    출력
    2
    """
{% endhighlight %}

## 풀이

DP를 사용해서 풀었다. dp 테이블을 n+1만큼 0으로 초기화를 해준다. 1 부터 n 까지 순회하며 dp 테이블을 i로 업데이트 해준다.
이후 i까지 while 문을 한번 더 순회한다. while 문을 순회하는 이유는 제곱수를 조회하기 위해서이다. 현재 i에서 뺄 수 있는 제곱수를 탐색해서 i에 빼준 dp를 탐색한다. 이후 더 작은 값을 dp[i]에 추가해준다.


## 코드

{% highlight python %}

    def solution(n):
        dp = [0] * (n+1)
        for i in range(1,n+1):
            dp[i] = i
            j = 1
            while j**2 <= i:
                if dp[i-j**2] + 1 < dp[i]:
                    dp[i] = dp[i-j**2] + 1
                j += 1
    
        return dp[n]
    
    
    if __name__ == "__main__":
        n = int(input())
        print(solution(n))
{% endhighlight %}