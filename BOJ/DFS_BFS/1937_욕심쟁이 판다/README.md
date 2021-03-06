# BOJ

## DFS/BFS 1937 욕심쟁이 판다
[문제로 이동!](https://www.acmicpc.net/problem/1937)

## 문제

n × n의 크기의 대나무 숲이 있다. 욕심쟁이 판다는 어떤 지역에서 대나무를 먹기 시작한다. 그리고 그 곳의 대나무를 다 먹어 치우면 상, 하, 좌, 우 중 한 곳으로 이동을 한다. 그리고 또 그곳에서 대나무를 먹는다. 그런데 단 조건이 있다. 이 판다는 매우 욕심이 많아서 대나무를 먹고 자리를 옮기면 그 옮긴 지역에 그 전 지역보다 대나무가 많이 있어야 한다.

이 판다의 사육사는 이런 판다를 대나무 숲에 풀어 놓아야 하는데, 어떤 지점에 처음에 풀어 놓아야 하고, 어떤 곳으로 이동을 시켜야 판다가 최대한 많은 칸을 방문할 수 있는지 고민에 빠져 있다. 우리의 임무는 이 사육사를 도와주는 것이다. n × n 크기의 대나무 숲이 주어져 있을 때, 이 판다가 최대한 많은 칸을 이동하려면 어떤 경로를 통하여 움직여야 하는지 구하여라.

## 입력

첫째 줄에 대나무 숲의 크기 n(1 ≤ n ≤ 500)이 주어진다. 그리고 둘째 줄부터 n+1번째 줄까지 대나무 숲의 정보가 주어진다. 대나무 숲의 정보는 공백을 사이로 두고 각 지역의 대나무의 양이 정수 값으로 주어진다. 대나무의 양은 1,000,000보다 작거나 같은 자연수이다.

## 예제 입력

{% highlight python %}

    """
    case 1:
    입력
    4
    14 9 12 10
    1 11 5 4
    7 15 2 13
    6 3 16 8
    출력
    4

    case 2:
    입력
    2
    1 4
    2 3
    출력
    4
    """
{% endhighlight %}

## 풀이

처음엔 graph의 모든 값을 순회하며 bfs로 최장거리의 max 값을 구했다. 하지만 bfs는 N^4 시간 복잡도를 가지기 때문에 시간초과가 난다. 시간초과를 해결하기 위해 dfs와 dp를 결합해서 문제를 해결해야한다.
bfs를 사용하지 않고 dfs를 사용하는 이유는 bfs는 이동할 수 있는 다음 칸의 위치를 큐에 넣고 나중에 탐색하며 반면에 dfs는 해당 위치에서 이동할 수 있는 모든 경로를 탐색하고 최장 경로의 길이를 반환하도록 만들 수 있으므로 비교적 dfs가 간단한다.

dfs를 사용해서 순차적으로 거리를 계산하면, 예를들어 (0,0) -> (0,1) -> (0,2) 순서로 탐색하게 된다면 visited에는 [1,2,3]이 저장 될 것이다. 하지만 우리가 원하는 것은 현재 위치에서의 최장 거리를 저장하는 것이기 때문에, dfs 함수를 호출한 뒤
거리를 계산하는 코드를 넣어준다. 그렇다면, 함수를 반환하면서 1씩 커지기 때문에 visited에는 [3,2,1] 이 저장 될 것이다. 또한, dfs 함수에 0을 만나게되면 return하게 되는 얼리리턴을 사용해서 탐색횟수를 줄여준다.


## 코드

{% highlight python %}

    import sys
    sys.setrecursionlimit(10**6)
    
    
    def dfs(x, y):
        if visited[x][y] != 0:
            return
        visited[x][y] = 1
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] > graph[x][y]:
                dfs(nx, ny)
                if visited[x][y] < visited[nx][ny] + 1:
                    visited[x][y] = visited[nx][ny] + 1
    
    
    if __name__ == "__main__":
        n = int(input())
        graph = [list(map(int, input().split())) for _ in range(n)]
        visited = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dfs(i, j)
        answer = max(map(max, visited))
        print(answer)
{% endhighlight %}