# BOJ

## 이진 탐색 2473 세 용액
[문제로 이동!](https://www.acmicpc.net/problem/2473)

## 문제

KOI 부설 과학연구소에서는 많은 종류의 산성 용액과 알칼리성 용액을 보유하고 있다. 각 용액에는 그 용액의 특성을 나타내는 하나의 정수가 주어져있다.  산성 용액의 특성값은 1부터 1,000,000,000까지의 양의 정수로 나타내고, 알칼리성 용액의 특성값은 -1부터 -1,000,000,000까지의 음의 정수로 나타낸다.

같은 양의 세 가지 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합으로 정의한다. 이 연구소에서는 같은 양의 세 가지 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 한다. 

예를 들어, 주어진 용액들의 특성값이 [-2, 6, -97, -6, 98]인 경우에는 특성값이 -97와 -2인 용액과 특성값이 98인 용액을 혼합하면 특성값이 -1인 용액을 만들 수 있고, 이 용액이 특성값이 0에 가장 가까운 용액이다. 참고로, 세 종류의 알칼리성 용액만으로나 혹은 세 종류의 산성 용액만으로 특성값이 0에 가장 가까운 혼합 용액을 만드는 경우도 존재할 수 있다.

산성 용액과 알칼리성 용액이 주어졌을 때, 이 중 같은 양의 세 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 세 용액을 찾는 프로그램을 작성하시오.

## 입력

첫째 줄에는 전체 용액의 수 N이 입력된다. N은 3 이상 5,000 이하의 정수이다. 둘째 줄에는 용액의 특성값을 나타내는 N개의 정수가 빈칸을 사이에 두고 주어진다. 이 수들은 모두 -1,000,000,000 이상 1,000,000,000 이하이다. N개의 용액들의 특성값은 모두 다르고, 산성 용액만으로나 알칼리성 용액만으로 입력이 주어지는 경우도 있을 수 있다.

## 예제 입력
{% highlight python %}

    """
    case 1:
    입력
    5
    -2 6 -97 -6 98
    출력
    -97 -2 98
    """
{% endhighlight %}

## 풀이
> 2467번의 용액과 비슷한 문제이다. 하지만 이는 세가지 수의 합이므로 기준 값을 하나 설정하고 나머지 값들을 two pointer를 활용해 해결한다. 우선 반복문을 돌며 가장 작은 값부터 기준 값으로 설정한다.
> 기준 값 + 1과 가장 큰 값인 N-1 을 start와 end 인자로 설정한다. 이후 start와 end의 폭을 좁혀가며 (기준 값 + start + end)의 절대값과 기존의 정답이 되는 최소 값의 절대값과 비교하여 작다면 정답 리스트에 저장해둔다.
> 이후 현재 값의 합이 0보다 작다면 start를 +1, 0보다 크다면 end를 -1 해준다. start와 end가 만나 while문을 탈출하게 되면 기준값을 하나 옮겨주고 반복한다.

## 코드

{% highlight python %}

    def two_pointer(array, basis, start, end):
        global value
        global answer
        while start < end:
            x = array[basis] + array[start] + array[end]
            if abs(value) > abs(x):
                value = x
                answer = [array[basis],array[start],array[end]]
            if x < 0:
                start += 1
            elif x > 0:
                end -= 1
            else:
                answer = [array[basis],array[start],array[end]]
                return True
        return False
    
    
    if __name__ == "__main__":
        n = int(input())
        array = list(map(int, input().split()))
        array.sort()
        value = array[0] + array[1] + array[2]
        answer = [array[0],array[1],array[2]]
        for i in range(n):
            if two_pointer(array, i, i+1, n-1):
                break
        print(*answer)
{% endhighlight %}