# 프로그래머스(Programmers) 코딩테스트 연습

## Level2 그리디 큰 수 만들기 파이썬(Python) 풀이

- https://programmers.co.kr/learn/courses/30/lessons/42748

## GitBlog 주소

- 

## 문제풀이
> 총 두가지의 방법으로 문제를 풀었는데 모두 테스트케이스 10에서 시간 초과로 인해 풀지 못하였다... 
> 그래서 정답 코드를 가지고 와서 공부를 하는 것으로 대신하겠다. 
> 파이썬에는 스택 자료구조가 따로 없고 리스트로 스택을 흉내내서 사용할 수 있다.
> 정답 코드는 스택의 성질을 사용하여서 문제를 해결했다.

### 맞는 풀이 solution3

1. stack을 흉내내는 리스트(stack이라 부르겠다.)에 number의 첫번째 값을 넣어준다(push).
2. number의 두번째 값부터 반복문을 돈다.
3. while문을 도는데, 조건은 세가지다.
    1. stack에 값이 있어야한다.
    2. stack의 마지막 값(stack.top)이 num보다 작아야한다.
    3. k가 0보다 커야한다.
4. 위에 해당하지 않으면 stack에 값을 추가해준다(push).
5. 조건이 해당하면, 반복문을 돌면서 stack.pop()과 k를 1씩 줄여준다.
6. 반복문이 끝나고도 k가 0이 아니면 stack을 뒤에서 k만큼 slicing해준다.
7. ''으로 join하여 문자열로 return한다.

### 틀린 풀이 solution1
1. numbur의 i와 i+1을 비교한다.
2. i가 i+1보다 작으면 i를 pop해준다.
3. 다시 첫번째 index로 돌아가 1-2번을 반복한다.
4. 남아있는 값이 len(number)-k의 길이가 아니면, 뒤에서 k만큼 slicing 해준다.
7. ''으로 join하여 문자열로 return한다.

### 틀린 풀이 solution2
1. number의 i와 j를 비교한다.
2. i가 j보다 작으면 i의 인덱스를 새로운 배열에 저장한다.
3. 모두 저장된 배열에 포함된 인덱스를 number에서 제거해준다.
4. 남아있는 값이 len(number)-k의 길이가 아니면, 뒤에서 k만큼 slicing 해준다.
7. ''으로 join하여 문자열로 return한다.


## 코드

{% highlight python %}

    def solution1(number, k):
        number = list(number)
        i = 0;
        while k > 0:
            for j in range(i,i+k+1):
                if number[i] == '9': break
                if number[i] < number[j]:
                    number.pop(i)
                    k = k -1
                    if i>0:
                        i = i -1
                        break
                    i = -1
                    break
            i += 1
        answer = ''.join(number)
        return answer
    
    def solution2(number, k):
        number = list(number)
        length = len(number)-k
        remove_list = []
        i = 0
        while k > 0:
            if i+1+k > len(number):
                break
            for j in range(i+1,i+1+k):
                if number[i] < number[j]:
                    remove_list.append(i)
                    k -= 1
                    break
            i += 1
        number = [number[i] for i in range(len(number)) if i not in remove_list]
        number = number[:length]
        answer = ''.join(number)
        return answer
    
    
    
    def solution3(number,k):
        stack = [number[0]]
        for num in number[1:]:
            while len(stack) > 0 and stack[-1] < num and k > 0:
                k -= 1
                stack.pop()
            stack.append(num)
        if k != 0:
            stack = stack[:-k]
        return ''.join(stack)
    
    
    if __name__ == "__main__":
        number = '4177252841'
        k = 4
        print(solution3(number, k))

{% endhighlight %}