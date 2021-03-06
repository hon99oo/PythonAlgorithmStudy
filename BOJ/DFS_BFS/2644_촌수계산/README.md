# BOJ

## DFS/BFS 2644 촌수계산
[문제로 이동!](https://www.acmicpc.net/problem/2644)

## 문제

우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 이러한 촌수는 다음과 같은 방식으로 계산된다. 기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다. 예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.

여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.

## 입력

사람들은 1, 2, 3, …, n (1 ≤ n ≤ 100)의 연속된 번호로 각각 표시된다. 입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고, 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다. 그리고 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다. 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다. 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.

각 사람의 부모는 최대 한 명만 주어진다.

## 예제 입력
{% highlight python %}

    """
    case 1:
    입력
    9
    7 3
    7
    1 2
    1 3
    2 7
    2 8
    2 9
    4 5
    4 6
    출력
    3

    case 2:
    입력
    9
    8 6
    7
    1 2
    1 3
    2 7
    2 8
    2 9
    4 5
    4 6
    출력
    -1
    """
{% endhighlight %}

## 풀이
> bfs로 찾고자 하는 두 개의 노드 사이를 계산 할 것이다. 찾고자 하는 두 개의 노드 중에서 기준 노드를 하나 잡는다. visited 리스트를 1로 초기화(1일 땐 방문하지 않은 것이다.)하고,
> 방문하게 되는 노드에 visited 리스트를 이전 노드에 저장된 값만큼 더해줄 것이다. 그렇다면 2 -> 3 -> 4 -> ... 순서로 기준 노드부터 기준 노드와 인접한 노드는 값이 저장될 것이다.
> 기준 노드와 찾고자 하는 노드의 인덱스를 뽑아서 -2를 해주면 정답을 도출할 수 있다.

### solution
1. visited 리스트를 1로 초기화해준다.
2. 찾고자하는 노드중 하나를 기준 값, 하나를 찾는 값으로 설정하고, bfs의 인자에 기준 값을 전해준다. 
3. bfs를 돌면서 방문하게 되는 노드의 visited 값에 해당 노드를 호출한 노드의 visited 값을 더해준다.
4. bfs 함수가 return 되면, 찾고자 하는 노드의 visited값 - 2를 출력해준다.

## 코드

{% highlight python %}

from collections import deque


    def bfs(v, graph, visited):
        queue = deque([v])
        visited[v] += 1
        while queue:
            v = queue.popleft()
            for i in graph[v]:
                if visited[i] == 1:
                    visited[i] = visited[i] + visited[v]
                    queue.append(i)
    
    
    if __name__ == "__main__":
        n = int(input())
        x, y = map(int, input().split())
        m = int(input())
    
        visited = [1] * (n+1)
        graph = []
        for _ in range(n+1):
            graph.append([])
    
        for _ in range(m):
            v1, v2 = map(int, input().split())
            graph[v1].append(v2)
            graph[v2].append(v1)
    
        bfs(x, graph, visited)
        print(visited[y] - 2)
{% endhighlight %}