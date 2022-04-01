# 이코테

## 그리디 만들 수 없는 금액(Python)

## 문제

N개의 동전을 갖고 있다.<br>
N개의 동전을 이용하여 만들 수 없는 정수 금액 중 최솟값을 구하라.<br>

- 예시

입력 : [3,2,1,1,9]<br>
결과 : 8
  
## 풀이
> 0과1이 인접한 부분이 몇개 있는지를 체크하면 된다. 예를들어 인접한 부분의 패턴을 '01'을 조사한다. 하지만, 1010 문자열을 조사하게 되면 마지막 인접한 부분을 조사하지 못해 최소 횟수가 1이 되므로
> 마지막 문자열에 1을 붙여주고 조사한다. 이렇게만 진행했을 경우 '010'을 조사하게 되면 최소 횟수가 2회가 된다. 그렇기 때문에 같은 방법으로 '01'과 '10'을 둘다 조사하여 두가지의 최소 횟수중 최소값을 구한다.

1. 문자열 S(str)의 마지막 부분을 조사해서 0 또는 1을 붙여준다.
2. 반복문을 돌며 '01'패턴과 '10'패턴을 조사한다 각각의 횟수를 count_0, count_1에 저장한다.
3. count_0과 count_1중 최소값을 return한다.



## 코드

{% highlight python %}

    def solution(array):
        array.sort()
        money_set = set()
        for i in range(len(array)):
            sum = 0
            for j in range(i,len(array)):
                sum += j
                money_set.add(sum)
    
        for i in range(max(money_set)):
            if i not in money_set:
                return i
        return max(money_set)+1
    
    def solution(array):
        array.sort()
        target = 1
        for x in array:
            if target < x:
                break
            target += x
    
        answer = target
    
    if __name__ == "__main__":
        array = [3,2,1,1,9]
        print(solution(array))

{% endhighlight %}