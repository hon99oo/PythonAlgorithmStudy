# 프로그래머스(Programmers) 코딩테스트 연습

## Level1 정렬 K번째수 파이썬(Python) 풀이

- https://programmers.co.kr/learn/courses/30/lessons/42862

## GitBlog 주소

- 

## 문제풀이
> 그리디 문제는 '현재 상황에서 지금 당장 좋은 것만 고르는 방법'을 의미한다. 알고리즘의 패턴보다는 풀이하는 사람의 아이디어가 더 중요한 알고리즘이다.
> 우선 체육복 문제는 인접한 index의 학생들만 여벌의 옷을 받을 수 있으므로 인접한 index에 대해서만 생각해주면 된다. 또한 도난당한 학생이 여벌의 옷을 가지고 올 수 있기 때문에
> 이 부분에서 예외처리를 해주어야한다.

1. lost와 reserve를 set형식으로 변경해준뒤 각각의 차집합을 구해준다.(도난당한 학생과 여벌옷을 가져온 학생이 중복된 경우를 제거하기 위해)
2. lost를 기준으로 

## 코드

{% highlight python %}

    def solution(n, lost, reserve):
        count = 0
        lost, reserve = list(set(lost)-set(reserve)), list(set(reserve)-set(lost))
        for lost_v in lost:
            for reserve_v in reserve:
                if lost_v - 1 == reserve_v or reserve_v == lost_v + 1:
                    reserve.remove(reserve_v)
                    count += 1
                    break
    
        answer = n - len(lost) + count
    
        return answer
    
    if __name__ == "__main__":
        n = 5
        lost = [1,2,4]
        reserve = [2,3,4,5]
        print(solution(n,lost,reserve))

{% endhighlight %}