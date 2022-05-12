# 이코테

## DP 1로 만들기(Python)

## 문제

정수 X가 주어질 때 정수 Xㅇㅔ 사용할 수 있는 연산은 다음과 같다.<br>
1. X가 5로 나누어 떨어지면, 5로 나눈다.
2. X가 3으로 나누어 떨어지면, 3으로 나눈다.
3. X가 2로 나누어 떨어지면, 2로 나눈다.
4. X에서 1을 뺀다.
정수 X가 연산 4개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력해라.
   
- 예시

입력 : 26<br>
결과 : 3
  
## 풀이
> 이 문제는 잘 알려진 다이나믹 프로그래밍 문제다. 

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