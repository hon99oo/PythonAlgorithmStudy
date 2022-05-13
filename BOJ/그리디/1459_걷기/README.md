# BOJ

## 그리디 1459_걷기

## 문제

세준이는 학교에서 집으로 가려고 한다. 도시의 크기는 무한대이고, 도시의 세로 도로는 모든 정수 x좌표마다 있고, 가로 도로는 모든 정수 y좌표마다 있다. 세준이는 현재 (0, 0)에 있다. 그리고 (X, Y)에 위치한 집으로 가려고 한다. 세준이가 걸을 수 있는 방법은 두가지 인데, 하나는 도로를 따라서 가로나 세로로 한 블록 움직여서 이번 사거리에서 저 사거리로 움직이는 방법이고, 블록을 대각선으로 가로지르는 방법이 있다.

세준이가 집으로 가는데 걸리는 최소시간을 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 집의 위치 X Y와 걸어서 한 블록 가는데 걸리는 시간 W와 대각선으로 한 블록을 가로지르는 시간 S가 주어진다. X와 Y는 1,000,000,000보다 작거나 같은 음이 아닌 정수이고, W와 S는 10,000보다 작거나 같은 자연수이다.

## 예제 입력
입력: 4 2 3 10, 출력: 18<br>
입력: 2 0 12 10, 출력: 20<br>
입력: 135 122 43 28, 출력: 3929<br>

## 풀이
> 

### solution1
1. 탐색하기 위해 노드를 저장하는 deque 변수를 선언한다.
    - deque는 (x좌표,y좌표,해당노드까지의 최단 거리) 가 tuple 형식으로 저장된다.
2. deque가 비게 되면 탈출하게 되는 while문을 선언한다.
3. 반복문을 돌며 첫번째로 deque를 pop하여 각각 x,y,v에 저장한다.
4. x와 y가 0보다 작거나 graph의 크기를 벗어나면 continue 해준다.
5. graph의 x, y좌표가 1이라면, 해당 노드에 v 값을 더해준다.
6. 이후 deque에 해당 좌표 기준 상,하,좌,우 값을 추가하여 탐색할 수 있게 설정한다.
7. 반복문이 끝나면 graph의 N,M 좌표에 해당하는 value를 return한다.

### solution2
> solution1과 로직은 같지만, solution2는 상하좌우를 배열에 저장하였고,
> 큐에는 x와 y좌표만 저장해두었다. 

## 코드

{% highlight python %}

    from collections import deque
    
    def solution1(graph):
        queue = deque([(0,0,0)])
        n = len(graph)
        m = len(graph[0])
    
        while queue:
            x,y,v = queue.popleft()
            if x>=n or y>=m or x<0 or y<0:
                continue
            if graph[x][y] == 1:
                graph[x][y] += v
                queue.append((x+1, y, graph[x][y]))
                queue.append((x, y+1, graph[x][y]))
                queue.append((x-1, y, graph[x][y]))
                queue.append((x, y-1, graph[x][y]))
    
        return graph[n-1][m-1]
    
    
    def solution2(graph):
        # 이동할 네 방향 정의(상, 하, 좌, 우)
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
    
        # graph 크기 정의
        n = len(graph)
        m = len(graph[0])
    
        # BFS 소스코드 구현
        def bfs(x, y):
    
            # 큐(Queue) 구현을 위해 deque 라이브러리 사용
            queue = deque()
            queue.append((x, y))
    
            # 큐가 빌 때까지 반복
            while queue:
                x, y = queue.popleft()
                # 현재 위치에서 네 방향으로의 위치 확인
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    # 미로 찾기 공간을 벗어난 경우 무시
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    # 벽인 경우 무시
                    if graph[nx][ny] == 0:
                        continue
                    # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                    if graph[nx][ny] == 1:
                        graph[nx][ny] = graph[x][y] + 1
                        queue.append((nx, ny))
    
            # 가장 오른쪽 아래까지의 최단 거리 반환
            return graph[n - 1][m - 1]
        
        return bfs(0,0)
    
    if __name__ == "__main__":
        graph = [
            [1,0,1,0,1,0],
            [1,0,1,1,1,1],
            [1,0,1,1,1,0],
            [1,0,1,0,1,0],
            [1,1,1,0,1,1]
        ]
        print(solution1(graph))

{% endhighlight %}