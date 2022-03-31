# 프로그래머스(Programmers) 코딩테스트 연습

## Level1 정렬 K번째수 파이썬(Python) 풀이

- https://programmers.co.kr/learn/courses/30/lessons/42748

## GitBlog 주소

- 

## 문제풀이
> python 에서 제공하는 list sort 관련 메소드를 잘 활용하면 쉽게 풀 수 있는 문제다.

1. 2차원 배열인 commands를 for 문을 돌려 1차원 배열을 인자로 받는다.
2. 1차원 배열에서 시작과 끝 index에 해당하는 index0 -1, index1로 array를 slicing 해준다.
3. slicing된 배열을 sorted해주고 x번째 값에 해당하는 index2로 값을 구해준다.
4. 구해진 값을 answer에 append한다.
5. return answer

## 코드

{% highlight python %}

    def solution(array, commands):
        answer = []
        for command in commands:
            answer.append(sorted(array[command[0]-1:command[1]])[command[2]-1])
        return answer
    
    if __name__ == "__main__":
        array = [1, 5, 2, 6, 3, 7, 4]
        commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
        print(solution(array, commands))

{% endhighlight %}