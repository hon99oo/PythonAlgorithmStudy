# BOJ

## 수학 1759 암호 만들기
[문제로 이동!](https://www.acmicpc.net/problem/1759)

## 문제

바로 어제 최백준 조교가 방 열쇠를 주머니에 넣은 채 깜빡하고 서울로 가 버리는 황당한 상황에 직면한 조교들은, 702호에 새로운 보안 시스템을 설치하기로 하였다. 이 보안 시스템은 열쇠가 아닌 암호로 동작하게 되어 있는 시스템이다.

암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다. 또한 정렬된 문자열을 선호하는 조교들의 성향으로 미루어 보아 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다. 즉, abc는 가능성이 있는 암호이지만 bac는 그렇지 않다.

새 보안 시스템에서 조교들이 암호로 사용했을 법한 문자의 종류는 C가지가 있다고 한다. 이 알파벳을 입수한 민식, 영식 형제는 조교들의 방에 침투하기 위해 암호를 추측해 보려고 한다. C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 두 정수 L, C가 주어진다. (3 ≤ L ≤ C ≤ 15) 다음 줄에는 C개의 문자들이 공백으로 구분되어 주어진다. 주어지는 문자들은 알파벳 소문자이며, 중복되는 것은 없다.

## 예제 입력

{% highlight python %}

    """
    case 1:
    입력
    4 6
    a t c i s w
    출력
    acis
    acit
    aciw
    acst
    acsw
    actw
    aist
    aisw
    aitw
    astw
    cist
    cisw
    citw
    istw
    """
{% endhighlight %}

## 풀이

백트래킹을 이용해서 문제를 해결했다. 우선 알파벳이 담겨있는 리스트를 오름차순으로 정렬한다.  visited 배열을 L 길이 만큼 초기화한다. 이후 dfs 함수를 돌면서 visited 첫번째 자리(depth)부터 탐색을 시작한다. 
visited 에 값이 들어있지 않다면, visited 첫번째 자리(depth)에 값을 추가해주고, depth +1, visited에 추가한 값의 index +1을 인자값으로 넘기면서 재귀적으로 dfs 함수를 호출한다.
정렬되어 있기 때문에, index+1을 함께 넘겨주어 해당 값 이후(즉, 증가하는 순서)만을 탐색하기 때문에 자동적으로 visited에 추가되는 값은 알파벳의 오름차순이다. 이후 depth가 l과 같아진다면, 모음과 자음의 개수를 확인하고 answer 리스트에 추가해준다.

## 코드

{% highlight python %}

    def dfs(string, depth, index, visited):
        global answer
        if depth == l:
            count = 0
            for v in visited:
                if v in collection:
                    count += 1
            if 1 <= count <= l-2:
                answer.append(visited.copy())
        else:
            for i in range(index, c):
                if string[i] in visited:
                    continue
                visited[depth] = string[i]
                dfs(string, depth+1, i+1, visited)
                visited[depth] = ''
    
    
    def solution(string):
        string.sort()
        visited = [''] * l
        dfs(string, 0, 0, visited)
    
    
    if __name__ == "__main__":
        l, c = map(int, input().split())
        string = list(map(str, input().split()))
        answer = []
        collection = {'a', 'e', 'i', 'o', 'u'}
        solution(string)
        for a in answer:
            print(''.join(a))
{% endhighlight %}