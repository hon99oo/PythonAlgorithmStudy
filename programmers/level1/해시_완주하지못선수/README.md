# 프로그래머스(Programmers) 코딩테스트 연습

## Level1 해시 완주하지 못한 선수 파이썬(Python) 풀이

- https://programmers.co.kr/learn/courses/30/lessons/42576

## GitBlog 주소

- 

## 문제풀이
> 딕셔너리에 선수의 이름을 key값으로, 중복된 선수의 이름을 체크하는 count를 value값으로 만들어준 뒤, 
> 완주한 선수의 목록을 반복문을 돌며 count를 1씩 줄이며 마지막으로 남아있는 선수를 출력하면 된다.
> 파이썬에서 딕셔너리는 해시테이블이라고 볼 수 있다.

### solution2(solved)
1. 딕셔너리 변수를 하나 지정해준다.
2. 참가자들의 반복문을 돌며 딕셔너리에 key값이 존재하지 않다면 value 0을, 존재한다면 value +1로 설정해준다.
3. 완주자들의 반복문을 돌며 딕셔너리에서 key값을 조회하며 value를 -1씩 해준다.
4. 반복문을 돌며 0보다 큰 값을 출력해준다.

### solution3(solved)
> hash값을 아주 잘 이용한 case여서 배워두면 유용하게 사용할 수 있을 것 같다.

1. 딕셔너리 변수를 하나 지정해준다.
2. 참가자들의 반복문을 돌며 딕셔너리 key값으로 참가자의 이름에 해당하는 hash값, value에는 참가자의 이름을 저장해준다.
3. 추가적으로 해당 hash값을 모두 더하여 저장하는 temp 변수를 만든다.
4. 완주자의 반복문을 돌며 완주자의 이름에 해당하는 hash값을 temp에서 계속 빼간다.
5. 이후 temp의 남아있는 값으로 딕셔너리의 key값을 조회한다.

## 새로 알게된 문법
>solution1은 시간초과로 문제를 해결하지 못하였는데 그 이유는 딕셔너리 컴프리헨션에서 사용한 count가 O(n) 시간을 가지고 있기 때문이다.

리스트 컴프리헨션만 존재하는 줄 알았지만, 컴프리헨션은 딕셔너리에서도 적용 가능했다.
{% highlight python %}
    a = {p:participant.count(p) for p in participant}
{% endhighlight %}

key:value 형식으로 저장한다.

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