# BOJ

## 그리디 11501 주식
[문제로 이동!](https://www.acmicpc.net/problem/11501)

## 문제

홍준이는 요즘 주식에 빠져있다. 그는 미래를 내다보는 눈이 뛰어나, 날 별로 주가를 예상하고 언제나 그게 맞아떨어진다. 매일 그는 아래 세 가지 중 한 행동을 한다.

주식 하나를 산다.
원하는 만큼 가지고 있는 주식을 판다.
아무것도 안한다.
홍준이는 미래를 예상하는 뛰어난 안목을 가졌지만, 어떻게 해야 자신이 최대 이익을 얻을 수 있는지 모른다. 따라서 당신에게 날 별로 주식의 가격을 알려주었을 때, 최대 이익이 얼마나 되는지 계산을 해달라고 부탁했다.

예를 들어 날 수가 3일이고 날 별로 주가가 10, 7, 6일 때, 주가가 계속 감소하므로 최대 이익은 0이 된다. 그러나 만약 날 별로 주가가 3, 5, 9일 때는 처음 두 날에 주식을 하나씩 사고, 마지막날 다 팔아 버리면 이익이 10이 된다.

## 입력

입력의 첫 줄에는 테스트케이스 수를 나타내는 자연수 T가 주어진다. 각 테스트케이스 별로 첫 줄에는 날의 수를 나타내는 자연수 N(2 ≤ N ≤ 1,000,000)이 주어지고, 둘째 줄에는 날 별 주가를 나타내는 N개의 자연수들이 공백으로 구분되어 순서대로 주어진다. 날 별 주가는 10,000이하다.

## 예제 입력
{% highlight python %}

    """
    입력
    3
    3
    10 7 6
    3
    3 5 9
    5
    1 1 3 1 2
    출력
    0
    10
    5
    """
{% endhighlight %}

## 풀이
> 첫쨋날 부터 계산을 하지 않고, 마지막날 부터 계산 하는 것이 해당 문제의 key point다. 주식 가격이 들어 있는 리스트를 스택이라고 가정하고 문제를 푼다.
> 마지막 날 주식 가격을 pop 해와서 제일 높은 가격이라고 가정하고 max값에 저장한다. 그다음 주식을 pop 해왔을 때 max값보다 작으면 max와의 차이를 benefit 리스트에 더해준다.
> max보다 크다면 max값을 변경해준다.

### solution
1. 이익을 저장할 리스트를 [0] * n 으로 초기화한다.
2. 먼저 주식 가격이 저장된 리스트를 pop 해서 max값에 저장한다.
3. 주식 가격이 저장된 리스트의 원소가 없어질 때 까지 while 문을 돌며 조건별로 처리해준다.

## 코드

{% highlight python %}

    def solution(n, stocks):
        benefit = [0] * n
        for s in range(n):
            max = stocks[s].pop()
            while stocks[s]:
                item = stocks[s].pop()
                if item <= max:
                    benefit[s] += max - item
                else:
                    max = item
    
        return benefit
    
    
    if __name__ == "__main__":
        n = int(input())
        stocks = []
        for _ in range(n):
            m = int(input())
            stocks.append(list(map(int, input().split())))
        result = solution(n, stocks)
        for r in result:
            print(r)
{% endhighlight %}