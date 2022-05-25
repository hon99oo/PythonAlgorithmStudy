# BOJ

## 수학 10974 모든 순열
[문제로 이동!](https://www.acmicpc.net/problem/10974)

## 문제

N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다. 

## 예제 입력

{% highlight python %}

    """
    case 1:
    입력
    3
    출력
    1 2 3
    1 3 2
    2 1 3
    2 3 1
    3 1 2
    3 2 1
    """
{% endhighlight %}

## 풀이
> 백트래킹을 사용해서 수열이 불가능한 지점에서 이전 지점으로 돌아가 탐색을 다시 진행하는 방법으로 해결한다. dfs 함수를 이용하여 문제를 해결하면된다. visited에 현재 탐색되는 수열을 저장하고, 탐색할 숫자가 있는지 체크한다.
> 모든 숫자를 체크하면 이전 자릿수로 돌아가 해당 숫자 이후로 탐색을 또 진행한다. 

## 코드

{% highlight python %}

    def dfs(depth, visited, n):
        global answer
    
        if depth == n:
            answer.append(visited.copy())
        else:
            for i in range(1, n+1):
                if i in visited:
                    continue
                visited[depth] = i
                dfs(depth + 1, visited, n)
                visited[depth] = 0
    
    
    if __name__ == "__main__":
        n = int(input())
        visited = [0] * n
        answer = []
        dfs(0, visited, n)
        for a in answer:
            print(*a)
{% endhighlight %}