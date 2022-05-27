# BOJ

## DP 11053 가장 긴 증가하는 부분 수열

[문제로 이동!](https://www.acmicpc.net/problem/11053)

## 문제

수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

## 입력

첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

## 예제 입력
{% highlight python %}

    """
    case 1:
    입력
    6
    10 20 10 30 20 50
    출력
    4

    case 2:
    입력
    50 10 20 10 20 30
    출력
    3
    """
{% endhighlight %}

## 풀이

DP로 문제를 해결했다. dp 테이블에는 해당 인자까지의 최대 길이를 저장한다. 이중 반복문을 돌며 dp 테이블을 업데이트한다. 

첫번째 반복문은 업데이트할 dp 테이블의 인덱스이며, 해당 인덱스를 인덱스-1 ~ 0 까지 돌면서 자신 보다 array 값이 작은 인자를 찾는다. 

작은 인자를 찾게 되면 해당 dp값과 현재 자신의 dp값중 큰 값을 자신의 dp 값으로 업데이트해준다.

## 코드

{% highlight python %}

    def solution(array, n):
        dp = [1] * n
        for i in range(1,n):
            for j in range(i-1, -1, -1):
                if array[i] > array[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
    
        return max(dp)
    
    
    if __name__ == "__main__":
        n = int(input())
        array = list(map(int, input().split()))
        print(solution(array, n))
{% endhighlight %}