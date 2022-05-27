# BOJ

## DP 9095 1,2,3 더하기
[문제로 이동!](https://www.acmicpc.net/problem/9095)

## 문제

정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

- 1+1+1+1
- 1+1+2
- 1+2+1
- 2+1+1
- 2+2
- 1+3
- 3+1

정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.

## 예제 입력
{% highlight python %}

    """
    case 1:
    입력
    3
    4
    7
    10  
    출력
    7
    44
    274 
    """
{% endhighlight %}

## 풀이

백트래킹을 사용해서 하나씩 경우의 수를 구해가며 문제를 풀었는데, DP는 점화식을 세워서 해결하는 문제다. 규칙을 찾아보면 n = f(n-1) + f(n-2) + f(n-3) 이기 때문에 solution2 코드로 간단하게도 해결할 수 있다.

규칙 : n = f(n-1) + f(n-2) + f(n-3)

1 -> 1개<br>
2 -> 2개<br>
3 -> 4개<br>
4 -> 7개(4+2+1)<br>
5 -> 13개(7+4+2)<br>


## 코드

{% highlight python %}

    # solution1: 백트래킹

    import sys
    sys.setrecursionlimit(10**6)
    
    
    def dfs(x, case, numbers):
        global count
        global answer
    
        sum_v = sum(case)
        if sum_v == x:
            if not case in answer:
                count += 1
                answer.append(case.copy())
            case.pop()
            return
        elif sum_v > x:
            case.pop()
            return
        else:
            for number in numbers:
                case.append(number)
                dfs(x, case, numbers)
    
        if len(case) > 0:
            case.pop()
    
        return
    
    if __name__ == "__main__":
        n = int(input())
        array = [int(input()) for _ in range(n)]
        numbers = [1,2,3]
        case = []
        count = 0
        flag = False
        answer = []
        for x in array:
            dfs(x, case, numbers)
            print(count)
            count = 0


    # solution2: DP

    def solution(v):
        if v == 1:
            return 1
        elif v == 2:
            return 2
        elif v == 3:
            return 4
        else:
            return solution(v-1) + solution(v-2) + solution(v-3)
    
    
    if __name__ == "__main__":
        n = int(input())
        array = [int(input()) for _ in range(n)]
    
        for v in array:
            print(solution(v))
{% endhighlight %}