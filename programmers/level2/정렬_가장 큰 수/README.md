# 프로그래머스(Programmers) 코딩테스트 연습

## Level2 정렬 가장 큰 수 파이썬(Python) 풀이

- https://programmers.co.kr/learn/courses/30/lessons/42746

## GitBlog 주소

- 

## 문제풀이
> 가장 큰 수를 만드려면, 예를 들어 9와 91이 있을 때 991이 919보다 더 큰 수가 된다. 
> 수의 가장 큰 값이 1000이기 때문에, ‘9’3, ‘91’3을 해서 비교를 하면, ‘999’ > ‘919191’ 이다. 
> 그렇기 때문에 int->str->*3을 하여 비교를 하여 정렬을 하고 해당 숫자들을 원래 숫자로 변경하여 return 해준다.

1. 배열의 값들을 str type으로 변경해준뒤 *3을 해준다.
2. 이후 sorted 함수를 사용하여 정렬한다.(내림차순으로 정렬하기 위해 reverse=True로 설정해준다.)
3. 다시 배열의 값들의 길이를 1/4로 나누어 slicing해준다.
4. 해당 배열들을 ‘‘로 join해준다.
5. return answer

## 코드

{% highlight python %}

    def solution(numbers):
        if sum(numbers)==0:
            return '0'
        numbers = sorted([str(number)*3 for number in numbers],reverse=True)
        answer = ''.join([numbers[i][:int(len(numbers[i])/4)] for i in range(len(numbers))])
        return answer
    
    if __name__ == "__main__":
        numbers = [6,2,10]
        print(solution(numbers))

{% endhighlight %}