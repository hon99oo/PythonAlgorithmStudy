# BOJ

## DP 1912 연속합

[문제로 이동!](https://www.acmicpc.net/problem/1912)

## 문제

n개의 정수로 이루어진 임의의 수열이 주어진다. 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다. 단, 수는 한 개 이상 선택해야 한다.

예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자. 여기서 정답은 12+21인 33이 정답이 된다.

## 입력

첫째 줄에 정수 n(1 ≤ n ≤ 100,000)이 주어지고 둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다. 수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

## 예제 입력
{% highlight python %}

    """
    case 1:
    입력
    10
    2 1 -4 3 4 -4 6 5 -5 1
    출력
    14

    case 2:
    입력
    5
    -1 -2 -3 -4 -5
    출력
    -1
    """
{% endhighlight %}

## 풀이

메모이제이션을 사용하여 문제를 해결한다. max_v(최대 값을 저장할 변수), dp[0](dp 테이블의 첫번째 값) 둘 모두 array[0]으로 초기화한다. 이후 1부터 n까지 반복문을 순회하며
dp테이블을 업데이트 하는데, 이전 dp 테이블 값과 현재 array의 값을 더한 값과 현재 array의 값을 비교해서 더 큰 값으로 dp값을 업데이트해준다.

array[i] 와 array[i]+dp[i-1] 을 비교하는 이유는, 음수를 만나도 그 다음 값이 훨씬 큰 양수면 음수를 이어서 더하는 것이 더 큰 값을 가지기 때문이다. 예를 들면, 10 -1 2000 이라면 이 세개의 숫자를 모두 이어서 더해야한다.
하지만, 음수를 더하지 않을 경우는 음수를 더한 뒤에 만나는 array의 현재 값보다 더한 값이 작아지면 음수를 더할 필요가 없기 때문에 현재 해당 array값 부터 다시 이어서 더하기 시작한다.

## 코드

{% highlight python %}

    def solution(array, n):
        dp = [0] * (n)
        dp[0] = array[0]
        max_v = array[0]
        for i in range(1, n):
            dp[i] = max(array[i], array[i] + dp[i-1])
            if max_v < dp[i]:
                max_v = dp[i]
    
        return max_v
    
    
    if __name__ == "__main__":
        n = int(input())
        array = list(map(int, input().split()))
        print(solution(array, n))
{% endhighlight %}