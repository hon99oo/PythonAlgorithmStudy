# 프로그래머스(Programmers) 코딩테스트 연습

## Level1 완전탐색 모의고사 파이썬(Python) 풀이

- https://programmers.co.kr/learn/courses/30/lessons/42840

## GitBlog 주소

- 

## 문제풀이
> 완전 탐색 문제다. 완전 탐색은 "컴퓨터의 빠른 계산을 이용하여 가능한 모든 경우의 수를 구하는 알고리즘"이다. 
> 문제를 어떻게 해결할지 방향을 잡고 최대한 빠른 로직으로 코드를 구현하는 것이 관건으로 보인다.

1. 사용자들의 정답 패턴을 각각의 배열에 저장한다.
2. 사용자들이 정답을 맞추는 개수를 저장하는 배열을 선언한다. (0으로 초기화한다.)
3. 사용자들의 정답 패턴의 length를 answers와의 나머지를 구하여 패턴을 일치시킨다.
4. 사용자들의 정답의 개수를 저장하고, 해당 배열의 max값을 찾는다.
5. max값과 일치하는 사용자들의 정답 개수를 갖는 index를 answer에 저장한다.
6. return answer

## 코드

{% highlight python %}

    def solution(answers):
        answer = []
        answer_list = [0,0,0]
        a = [1, 2, 3, 4, 5]
        b = [2, 1, 2, 3, 2, 4, 2, 5]
        c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
        for i in range(len(answers)):
            if a[i%len(a)]==answers[i]:
                answer_list[0]+=1
            if b[i%len(b)]==answers[i]:
                answer_list[1]+=1
            if c[i%len(c)]==answers[i]:
                answer_list[2]+=1
    
        for i,val in enumerate(answer_list):
            if val == max(answer_list):
                answer.append(i+1)
        return answer
    
    if __name__ == "__main__":
        answers = [5, 5, 4, 2, 3]
        print(solution(answers))

{% endhighlight %}