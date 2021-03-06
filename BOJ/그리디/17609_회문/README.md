# BOJ

## 그리디 17609 회문
[문제로 이동!](https://www.acmicpc.net/problem/17609)

## 문제

회문(回文) 또는 팰린드롬(palindrome)은 앞 뒤 방향으로 볼 때 같은 순서의 문자로 구성된 문자열을 말한다. 예를 들어 ‘abba’ ‘kayak’, ‘reviver’, ‘madam’은 모두 회문이다. 만일 그 자체는 회문이 아니지만 한 문자를 삭제하여 회문으로 만들 수 있는 문자열이라면 우리는 이런 문자열을 “유사회문”(pseudo palindrome)이라고 부른다. 예를 들어 ‘summuus’는 5번째나 혹은 6번째 문자 ‘u’를 제거하여 ‘summus’인 회문이 되므로 유사회문이다.

여러분은 제시된 문자열을 분석하여 그것이 그 자체로 회문인지, 또는 한 문자를 삭제하면 회문이 되는 “유사회문”인지, 아니면 회문이나 유사회문도 아닌 일반 문자열인지를 판단해야 한다. 만일 문자열 그 자체로 회문이면 0, 유사회문이면 1, 그 외는 2를 출력해야 한다. 

## 입력

입력의 첫 줄에는 주어지는 문자열의 개수를 나타내는 정수 T(1 ≤ T ≤ 30)가 주어진다. 다음 줄부터 T개의 줄에 걸쳐 한 줄에 하나의 문자열이 입력으로 주어진다. 주어지는 문자열의 길이는 3 이상 100,000 이하이고, 영문 알파벳 소문자로만 이루어져 있다.

## 예제 입력
{% highlight python %}

    """
    입력
    7
    abba
    summuus
    xabba
    xabbay
    comcom
    comwwmoc
    comwwtmoc
    출력
    0
    1
    1
    2
    2
    0
    1
    """
{% endhighlight %}

## 풀이
> 회문은 양 끝부터 차례대로 확인해야 하기 때문에 <strong>투 포인터</strong>를 사용한다. 다른 문자를 만나게 되면 start 포인터를 pop 하는 경우와 end 포인터를 pop 하는 경우 두가지를 
> 계산한다. 이 계산에서 한번 더 다른 문자를 만나게 되면 더 이상 계산할 필요가 없기 때문에 break를 걸어 전체 반복문을 탈출해서 답을 도출한다.

### solution
1. start 포인터를 pop 할 때 계산하는 함수와 end 포인터를 pop 할 때 계산하는 함수를 정의한다. (함수를 사용하는 이유는 전체 반복문을 편리하게 탈출하기 위해서이다.)
2. 스타트 포인터가 해당 string의 중간지점에 위치할 때 까지 while문을 돈다.
3. 다른 문자를 만나게 되면 count를 1 올려주고 start_pop 함수와 end_pop 함수를 호출한다.
4. 각각의 함수에서 다른 문자를 만나게 되면 count를 2로 설정해서 리턴한다.
5. 각각 함수를 호출하고 난뒤 리턴 받은 count(count_sp, count_ep)중 최소값을 count에 저장한 뒤 break로 반복문을 빠져나온다.
6. count를 결과 리스트에 저장해서 return 한다.

## 코드

{% highlight python %}

    import sys
    
    
    def start_pop(string, start, end):
        start += 1
        while start < len(string)//2 + 1:
            if string[start] != string[end]:
                return 2
            start += 1
            end -= 1
        return 1
    
    
    def end_pop(string, start, end):
        end -= 1
        while start < len(string)//2:
            if string[start] != string[end]:
                return 2
            start += 1
            end -= 1
        return 1
    
    
    def solution(strings):
        result = []
    
        for string in strings:
            count = 0
            start = 0
            end = len(string)-1
            while start < len(string)//2:
                if string[start] != string[end]:
                    count_sp = start_pop(string, start, end)
                    count_ep = end_pop(string, start, end)
                    count = min(count_ep, count_sp)
                    break
                start += 1
                end -= 1
            result.append(count)
        return result
    
    
    
    if __name__ == "__main__":
        n = int(input())
        strings = []
        for _ in range(n):
            strings.append(sys.stdin.readline().rstrip())
        results = solution(strings)
        for result in results:
            print(result)
{% endhighlight %}