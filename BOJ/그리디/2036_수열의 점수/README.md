# BOJ

## 그리디 2036 수열의 점수
[문제로 이동!](https://www.acmicpc.net/problem/2036)

## 문제

n개의 정수로 이루어진 수열이 있다. 이 수열에서 한 정수를 제거하거나, 또는 두 정수를 제거할 수 있다. 한 정수를 제거하는 경우에는 그 정수가 점수가 되고, 두 정수를 제거하는 경우에는 두 정수의 곱이 점수가 된다. 이를 반복하여 수열에 아무 수도 남지 않게 되었을 때, 점수의 총 합의 최대를 구하는 프로그램을 작성하시오.

예를 들어 -1, 5, -3, 5, 1과 같은 수열이 있다고 하자. 먼저 1을 제거하고, 다음으로는 5와 5를 제거하고, 다음에는 -1과 -3을 제거했다고 하자. 이 경우 각각 점수가 1, 25, 3이 되어 총 합이 29가 된다.

## 입력

첫째 줄에 정수 n(1 ≤ n ≤ 100,000)이 주어진다. 다음 n개의 줄에는 절댓값이 1,000,000을 넘지 않는 정수가 n개 주어진다.

## 예제 입력
{% highlight python %}

    """
    입력
    5
    -1
    5
    -3
    5
    1
    출력
    29
    """
{% endhighlight %}

## 풀이
> 양수 부분과 음수 부분을 나누어서 해결해야한다. 우선 0은 양수 부분에 있으면 최대값을 찾는데 도움을 주지 않는다. 그렇기 때문에 0음 음수 부분으로 나누어 준다.
> 또한 나뉘어진 부분의 개수가 홀수라면 음수 중에서는 제일 큰 수가 더해져야하고, 양수 중에서는 제일 작은 수가 더해져야한다. 이후 이 모두를 합산하면 결과값이 나온다.

### solution
1. 우선 입력받은 numbers 리스트를 정렬해준다.
2. numbers를 반복문을 돌며 음수 부분과 양수 부분으로 나누어준다.
3. 음수 부분이 짝수 개수라면 모두 두개씩 곱해준다.
4. 음수 부분이 홀수 개수라면 negative_n-1에 위치한 값을 제외하고 모두 곱해준뒤 해당 값은 더해준다.
5. 양수 부분이 짝수 개수라면 모두 두개씩 곱해준다.
6. 양수 부분이 홀수 개수라면 0에 위치한 값을 제외하고 모두 곱해준뒤 해당 값은 더해준다.

## 코드

{% highlight python %}

    def solution(numbers):
        numbers.sort()
        result = 0
        negative_list = []
        positive_list = []
        negative_n = 0
        positive_n = 0
    
        for n in numbers:
            if n <= 0:
                negative_list.append(n)
                negative_n += 1
            else:
                positive_list.append(n)
                positive_n += 1
    
        if negative_n % 2 == 0:
            for i in range(0,negative_n, 2):
                result += negative_list[i] * negative_list[i+1]
        else:
            for i in range(0, negative_n-1, 2):
                result += negative_list[i] * negative_list[i+1]
            result += negative_list[negative_n-1]
    
        if positive_n % 2 == 0:
            for i in range(0, positive_n, 2):
                if positive_list[i] > 1 and positive_list[i+1] >1:
                    result += positive_list[i] * positive_list[i+1]
                else:
                    result += positive_list[i] + positive_list[i+1]
        else:
            for i in range(1, positive_n, 2):
                if positive_list[i] > 1 and positive_list[i+1] >1:
                    result += positive_list[i] * positive_list[i+1]
                else:
                    result += positive_list[i] + positive_list[i+1]
            result += positive_list[0]
    
    
        return result
    
    
    if __name__ == "__main__":
        n = int(input())
        numbers = []
        for _ in range(n):
            numbers.append(int(input()))
        print(solution(numbers))
{% endhighlight %}