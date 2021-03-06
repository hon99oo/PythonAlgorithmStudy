# BOJ

## 이진 탐색 2467 용액
[문제로 이동!](https://www.acmicpc.net/problem/2467)

## 문제

KOI 부설 과학연구소에서는 많은 종류의 산성 용액과 알칼리성 용액을 보유하고 있다. 각 용액에는 그 용액의 특성을 나타내는 하나의 정수가 주어져있다. 산성 용액의 특성값은 1부터 1,000,000,000까지의 양의 정수로 나타내고, 알칼리성 용액의 특성값은 -1부터 -1,000,000,000까지의 음의 정수로 나타낸다.

같은 양의 두 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합으로 정의한다. 이 연구소에서는 같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 한다. 

예를 들어, 주어진 용액들의 특성값이 [-99, -2, -1, 4, 98]인 경우에는 특성값이 -99인 용액과 특성값이 98인 용액을 혼합하면 특성값이 -1인 용액을 만들 수 있고, 이 용액의 특성값이 0에 가장 가까운 용액이다. 참고로, 두 종류의 알칼리성 용액만으로나 혹은 두 종류의 산성 용액만으로 특성값이 0에 가장 가까운 혼합 용액을 만드는 경우도 존재할 수 있다.

산성 용액과 알칼리성 용액의 특성값이 정렬된 순서로 주어졌을 때, 이 중 두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액을 찾는 프로그램을 작성하시오.

## 입력

첫째 줄에는 전체 용액의 수 N이 입력된다. N은 2 이상 100,000 이하의 정수이다. 둘째 줄에는 용액의 특성값을 나타내는 N개의 정수가 빈칸을 사이에 두고 오름차순으로 입력되며, 이 수들은 모두 -1,000,000,000 이상 1,000,000,000 이하이다. N개의 용액들의 특성값은 모두 서로 다르고, 산성 용액만으로나 알칼리성 용액만으로 입력이 주어지는 경우도 있을 수 있다.

## 예제 입력
{% highlight python %}

    """
    case 1:
    입력
    5
    -99 -2 -1 4 98
    출력
    -99 98
    """
{% endhighlight %}

## 풀이
> two pointer를 사용하여 문제를 해결했다. start와 end를 배열의 양 끝으로 설정한다. 그렇다면 start는 가장 작 음수값을 가지며, end는 가장 큰 양수값을 가진다. 이 폭을 좁혀가며 탐색할 것이다.
> start와 end에 해당하는 인자의 합의 절대값과 기존의 min의 절대값을 비교하여 현재 인자들의 합이 더 작다면 정답 리스트에 저장해둔다.
> 또한 현재 인자의 합이 0보다 크다면 end를 1씩 줄이고, 0보다 작다면 start를 1씩 줄인다.

## 코드

{% highlight python %}

    def binary_search(array, start, end):
        value = array[0] + array[1]
        answer = [array[0], array[1]]
        while start < end:
            x = array[start] + array[end]
            if abs(x) < abs(value):
                value = x
                answer = [array[start], array[end]]
            if x < 0:
                start += 1
            elif x > 0:
                end -= 1
            else:
                break
    
        return answer
    
    
    if __name__ == "__main__":
        n = int(input())
        array = list(map(int, input().split()))
        start = 0
        end = n-1
        print(*binary_search(array, start, end))
{% endhighlight %}