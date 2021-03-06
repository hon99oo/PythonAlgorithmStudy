# BOJ

## 이진 탐색 16401 과자 나눠주기
[문제로 이동!](https://www.acmicpc.net/problem/16401)

## 문제

명절이 되면, 홍익이 집에는 조카들이 놀러 온다. 떼를 쓰는 조카들을 달래기 위해 홍익이는 막대 과자를 하나씩 나눠준다.

조카들이 과자를 먹는 동안은 떼를 쓰지 않기 때문에, 홍익이는 조카들에게 최대한 긴 과자를 나눠주려고 한다.

그런데 나눠준 과자의 길이가 하나라도 다르면 조카끼리 싸움이 일어난다. 따라서 반드시 모든 조카에게 같은 길이의 막대 과자를 나눠주어야 한다.

M명의 조카가 있고 N개의 과자가 있을 때, 조카 1명에게 줄 수 있는 막대 과자의 최대 길이를 구하라.

단, 막대 과자는 길이와 상관없이 여러 조각으로 나눠질 수 있지만, 과자를 하나로 합칠 수는 없다. 단, 막대 과자의 길이는 양의 정수여야 한다.

## 입력

첫째 줄에 조카의 수 M (1 ≤ M ≤ 1,000,000), 과자의 수 N (1 ≤ N ≤ 1,000,000)이 주어진다.

둘째 줄에 과자 N개의 길이 L1, L2, ..., LN이 공백으로 구분되어 주어진다. 과자의 길이는 (1 ≤ L1, L2, ..., LN ≤ 1,000,000,000) 를 만족한다.

## 예제 입력
{% highlight python %}

    """
    case 1:
    입력
    3 10
    1 2 3 4 5 6 7 8 9 10
    출력
    8

    case 2:
    입력
    4 3
    10 10 15
    출력
    7
    """
{% endhighlight %}

## 풀이

> 파라메트릭 서치(parametric search)를 사용해서 풀었다. mid 값을 조사하고 답이 되지 않는다면 그 이하 또는 이상은 답이 되지 않는다고 판단하는 방법이다.
> mid 값에서 과자를 나눠줄 수 있는 경우의 수를 구한 뒤 target과 비교하고 mid 값을 조절해준다. mid값과 target이 같아 진다면 answer에 저장해둔 뒤 mid값을 또 조사해 최적의 answer를 탐색한다.

## 코드

{% highlight python %}

    def upper_bound(start, end, target):
        result = 0
        while start <= end:
            mid = (start + end) // 2
            sum_v = sum(map(lambda x: x//mid, array))
            if sum_v >= target:
                start = mid + 1
                result = mid
            else:
                end = mid - 1
        return result
    
    
    if __name__ == "__main__":
        n, m = map(int, input().split())
        array = list(map(int, input().split()))
        if sum(array) < n:
            print(0)
        else:
            print(upper_bound(1,max(array),n))
{% endhighlight %}