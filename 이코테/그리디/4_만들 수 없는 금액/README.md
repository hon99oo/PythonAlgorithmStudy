# 이코테

## 그리디 만들 수 없는 금액(Python)

## 문제

N개의 동전을 갖고 있다.<br>
N개의 동전을 이용하여 만들 수 없는 정수 금액 중 최솟값을 구하라.<br>

- 예시

입력 : [3,2,1,1,9]<br>
결과 : 8
  
## 풀이
> 고민을 좀 많이 했던 문제이다. 만들 수 있는 금액을 모두 구한 뒤 해당 금액에서 없는 금액중 최소값을 구하는 방식으로 접근했었다.
> 이렇게 문제를 풀면 n^2의 시간이 걸린다. 하지만, 해답에서는 n으로 풀고 있어 정답 코드를 배울 필요성이 있어 보인다.
> 정답 코드는 누적합을 사용한다.
 
### solution1
1. 동전이 모두 저장되어 있는 array를 정렬한다.
2. 동전들의 모든 가능한 합이 저장될 set 타입의 변수를 선언한다. (set은 중복이 없다.)
3. 1,1,2,3,9라면, 1, 1+1, 1+1+2, 1+1+2+3, 1+1+2+3+9 \\ 1, 1+2, 1+2+3, 1+2+3+9 \\ 2, 2+3, ... 식으로 
2중 포문을 돌리며 값을 저장한다.
4. 이후 set의 max값 만큼 반복문을 돌며 만들 수 없는 최솟값을 구한다.
5. 4번에서 구한 최소값을 return한다.

### solution2
1. 동전이 모두 저장되어 있는 array를 정렬한다.
2. target=1을 선언한다.(0인 동전은 없기 때문에)
3. array를 반복문을 돌며 동전을 하나씩 꺼낸다.
4. target이 동전보다 작다면 break 한다.(더이상 만들 수 없는 동전을 만났기 때문)
5. target이 동전보다 작지 않다면 target에 동전을 더해준다.
6. 반복문을 빠져나오면 target을 return한다.

> 모든 것을 다 구해야만 가능하다고 생각해서 이중 포문을 돌았지만, 
> 누적된 합은 다시 구해도 되지 않은 수이기 때문에 부등호를 사용하여 비교한 점이 인상 깊었다.


## 코드

{% highlight python %}

    def solution1(array):
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
    
    def solution2(array):
        array.sort()
        target = 1
        for x in array:
            if target < x:
                break
            target += x
    
        answer = target
    
    if __name__ == "__main__":
        array = [3,2,1,1,9]
        print(solution2(array))

{% endhighlight %}