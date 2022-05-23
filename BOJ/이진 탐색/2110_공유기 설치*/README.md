# BOJ

## 이진 탐색 2110 공유기 설치
[문제로 이동!](https://www.acmicpc.net/problem/2110)

## 문제

도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.

도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

## 입력

첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.

## 예제 입력
{% highlight python %}

    """
    case 1:
    입력
    5 3
    1
    2
    8
    4
    9
    출력
    3
    """
{% endhighlight %}

## 풀이
> 공유기 설치의 거리를 이진탐색으로 좁혀가거나 넓혀가거나로 탐색해나가며 문제를 풀어간다. 공유기 거리의 최소값을 1, 최대값을 index0에서 마지막값을 뺀 값으로 설정한다.
> mid값이 설정되면 해당 거리를 집마다 설치할 수 있는 개수가 C보다 작다면 거리를 좁혀야하고, C보다 크다면 거리를 넓혀야 한다. prametric search로 정답을 저장해가며 탐색한다.

## 코드

{% highlight python %}

    def binary_search(array, start, end):
        result = 0
        while start <= end:
            mid = (start + end) // 2
            value = array[0]
            count = 1
            for i in range(1,n):
                if array[i] >= value +mid:
                    value = array[i]
                    count +=1
            if count >= c:
                start = mid + 1
                result = mid
            else:
                end = mid - 1
    
        return result
    
    
    if __name__ == "__main__":
        n, c = map(int, input().split())
        array = []
        for _ in range(n):
            array.append(int(input()))
        array.sort()
        end = array[-1] - array[0]
        print(binary_search(array, 1, end))
{% endhighlight %}