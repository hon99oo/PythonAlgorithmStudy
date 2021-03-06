# BOJ

## DFS/BFS 1260 DFS와 BFS
[문제로 이동!](https://www.acmicpc.net/problem/1260)

## 문제

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

## 입력

첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

## 예제 입력
{% highlight python %}

    """
    case 1:
    입력
    4 5 1
    1 2
    1 3
    1 4
    2 4
    3 4
    출력
    1 2 4 3
    1 2 3 4

    case 2:
    입력
    5 5 3
    5 4
    5 2
    1 2
    3 4
    3 1  
    출력
    3 1 2 5 4
    3 1 4 2 5
    """
{% endhighlight %}

## 풀이
> DFS와 BFS를 사용하면 간단히 풀 수 있는 문제이다. 하지만, 입력값으로부터 인접리스트 그래프를 만들 때 들어가는 인자값을 sorting을 해주어야 정확한 순서로 그래프를 탐색한다.

### solution
1. bfs와 dfs 함수를 정의한다.
2. 인접리스트 graph를 초기화한다.
3. 입력값을 저장하고 해당 리스트를 정렬한다.
4. bfs와 dfs 함수를 호출해 정답을 도출한다.


## 새로 배운점
- 리스트에 *을 붙여서 print하면 c언어 처럼 출력된다.
- graph 인접리스트를 만들 때 heapq로 생성하면 리스트 후 정렬 하는 것보다 성능이 아주 조금 더 좋다.

## 코드

{% highlight python %}

    from collections import deque
    
    
    def dfs(v):
        visited_dfs[v] = True
        order_dfs.append(v)
        for i in graph[v]:
            if not visited_dfs[i]:
                dfs(i)
    
    
    def bfs(v):
        visited_bfs[v] = True
        order_bfs.append(v)
        queue = deque([v])
        while queue:
            x = queue.popleft()
            for i in graph[x]:
                if not visited_bfs[i]:
                    visited_bfs[i] = True
                    order_bfs.append(i)
                    queue.append(i)
    
    
    if __name__ == "__main__":
        n, m, start = map(int, input().split())
        graph = []
        for _ in range(n+1):
            graph.append([])
    
        for _ in range(m):
            x, y = map(int, input().split())
            graph[x].append(y)
            graph[x].sort()
            graph[y].append(x)
            graph[y].sort()
    
    
        visited_dfs = [False] * (n+1)
        order_dfs = []
        visited_bfs = [False] * (n+1)
        order_bfs = []
    
        dfs(start)
        print(*order_dfs)
        bfs(start)
        print(*order_bfs)
{% endhighlight %}