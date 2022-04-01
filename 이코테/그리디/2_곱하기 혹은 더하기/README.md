# 이코테

## 그리디 곱하기 혹은 더하기(Python)

## 문제

숫자로만 이루어진 문자열 S가 있다.<br>
숫자 사이에 'x', '+' 연산자를 넣어 가장 큰 수를 만들어라.<br>

- 예시

입력 : '02984'
결과 : 576
  
## 풀이
> 0과 1일 때는 +를 해주고 그렇지 않으면 x를 해주는 것이 이 문제의 포인트로 보인다.

1. sum 변수에 str(문자열 S)의 첫번째 인덱스의 값을 넣어준다.
2. str의 두번째 인덱스의 값부터 반복문을 돌린다.
3. sum과 ch(반복문을 도는 str의 값)이 2보다 작다면 +, 그렇지 않으면 x를 해준다.
    - sum도 체크 하는 이유는 sum이 0이나 1이면 +를 해줘야 하기 때문
4. return sum


## 코드

{% highlight python %}

    def solution(str):
        sum = int(str[0])
    
        for ch in str[1:]:
            ch = int(ch)
            if sum < 2 or ch < 2:
                sum += ch
            else:
                sum *= ch
    
        return sum
    
    
    if __name__ == "__main__":
        str = "567"
        print(solution(str))

{% endhighlight %}