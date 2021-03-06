# BOJ

## DFS/BFS 14504 로봇 청속
[문제로 이동!](https://www.acmicpc.net/problem/14503)

## 문제

로봇 청소기가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.

로봇 청소기가 있는 장소는 N×M 크기의 직사각형으로 나타낼 수 있으며, 1×1크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 벽 또는 빈 칸이다. 청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북중 하나이다. 지도의 북쪽에서부터 r번째, 서쪽에서부터 c번째로 위치한 칸은 (r, c)로 나타낼 수 있다.

로봇 청소기는 다음과 같이 작동한다.

1. 현재 위치를 청소한다.
2. 현재 위치에서 다음을 반복하면서 인접한 칸을 탐색한다.
    a. 현재 위치의 바로 왼쪽에 아직 청소하지 않은 빈 공간이 존재한다면, 왼쪽 방향으로 회전한 다음 한 칸을 전진하고 1번으로 돌아간다. 그렇지 않을 경우, 왼쪽 방향으로 회전한다. 이때, 왼쪽은 현재 바라보는 방향을 기준으로 한다.
    b. 1번으로 돌아가거나 후진하지 않고 2a번 단계가 연속으로 네 번 실행되었을 경우, 바로 뒤쪽이 벽이라면 작동을 멈춘다. 그렇지 않다면 한 칸 후진한다.

## 입력

첫째 줄에 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 50)

둘째 줄에 로봇 청소기가 있는 칸의 좌표 (r, c)와 바라보는 방향 d가 주어진다. d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을 바라보고 있는 것이다.

셋째 줄부터 N개의 줄에 장소의 상태가 북쪽부터 남쪽 순서대로, 각 줄은 서쪽부터 동쪽 순서대로 주어진다. 빈 칸은 0, 벽은 1로 주어진다. 지도의 첫 행, 마지막 행, 첫 열, 마지막 열에 있는 모든 칸은 벽이다.

로봇 청소기가 있는 칸의 상태는 항상 빈 칸이다.

## 예제 입력
{% highlight python %}

    """
    case 1:
    입력
    3 3
    1 1 0
    1 1 1
    1 0 1
    1 1 1
    출력
    1

    case 2:
    입력
    11 10
    7 4 0
    1 1 1 1 1 1 1 1 1 1
    1 0 0 0 0 0 0 0 0 1
    1 0 0 0 1 1 1 1 0 1
    1 0 0 1 1 0 0 0 0 1
    1 0 1 1 0 0 0 0 0 1
    1 0 0 0 0 0 0 0 0 1
    1 0 0 0 0 0 0 1 0 1
    1 0 0 0 0 0 1 1 0 1
    1 0 0 0 0 0 1 1 0 1
    1 0 0 0 0 0 0 0 0 1
    1 1 1 1 1 1 1 1 1 1
    출력
    57  
    """
{% endhighlight %}

## 풀이
> 구현으로 해결하였다. 문제에서는 0이 북쪽, 1이 동쪽, 2가 남쪽, 3이 서쪽이지만, 풀이 편의상 동쪽과 서쪽의 번호를 바꾸었다. 이렇게 할 경우, 0~3의 방향 순서가 로봇 청소기가 탐색을 위해 회전하는 방향의 순서와 같아지므로
> 반복문으로 코드를 줄일 수 있다. 로봇청소기가 상,하,좌,우를 탐색하고 0이 있다면 진행후 방향을 진행 방향으로 업데이트, 모두 탐색해도 0이 없다면 현재 방향의 뒤를 탐색하고 벽이 아니라면 방향을 현재 방향으로 업데이트하고 뒤로 이동한다.(후진)
> 이후 벽을 만나게 되면 현재 count로 리턴한다.

<img src="img_1.png" width="50%" height="100%">

> DFS로도 문제를 해결할 수 있다고 한다.

## 코드

{% highlight python %}

    from collections import deque
    
    
    def solution(r, c, d, graph):
        graph[r][c] = -1
        count = 1
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        queue = deque()
        queue.append((r, c))
        while queue:
            flag = 0
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[(d + i) % 4]
                ny = y + dy[(d + i) % 4]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if graph[nx][ny] == 0:
                    queue.append((nx, ny))
                    graph[nx][ny] = -count
                    count += 1
                    flag = 1
                    d = (d+i+1) % 4
                    break
            if flag == 0:
                nx = x + dx[(d+1) % 4]
                ny = y + dy[(d+1) % 4]
                if graph[nx][ny] == 1:
                    return count
                else:
                    graph[nx][ny] = -1
                    queue.append((nx, ny))
    
        return count
    
    
    if __name__ == "__main__":
        n, m = map(int, input().split())
        r, c, d = map(int, input().split())
        if d == 1:
            d = 3
        elif d == 3:
            d = 1
    
        graph = []
        for _ in range(n):
            graph.append(list(map(int, input().split())))
        print(solution(r, c, d, graph))
{% endhighlight %}