# 이코테

## DFS/BFS 미로 탈출(Python)

## 문제

N x M 크기의 미로가 있다.<br>
몬스터가 있는 곳은 0, 몬스터가 없는 곳은 1로 표시된다.<br>
몬스터를 피해서 (0,0) 좌표에서 (N,M) 좌표까지 탈출해야한다.<br>
이때 탈출까지의 최단 거리를 구하여라.

- 예시<br>

입력 : <br>
    [1,0,1,0,1,0]<br>
    [1,0,1,1,1,1]<br>
    [1,0,1,1,1,0]<br>
    [1,0,1,0,1,0]<br>
    [1,1,1,0,1,1]<br>
결과 : 14

## 풀이
> 이 문제는 1이 연결된 길을 찾으면 되는 문제이다. 최단 거리를 구하기 위해서 현재 위치에서 근접한 1의 위치를 찾으면 된다. 
> 하지만, 관건은 근접한 1의 위치를 찾고 최단거리를 계산하는 방법이다.
> 1을 만나게 되면, 이전 노드의 정보를 더해주는 방식으로 (1,1) 좌표에서 특정 노드까지의 최단거리를 모두 저장해주면 된다.
> 이후 (N,M)에 저장되어 있는 정보를 출력하면 된다.

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