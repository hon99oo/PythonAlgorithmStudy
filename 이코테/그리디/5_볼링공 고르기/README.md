# 이코테

## 그리디 볼링공 고르기(Python)

## 문제

두 사람이 서로 다른 무게의 볼링공을 고르려고 한다.<br>
같은 무게의 공이 여러개 있따면 서로 다른 공으로 간주된다.<br>
이 때 두 사람이 고를 수 있는 볼링공 번호의 조합의 경우의 수를 구하라.


- 예시

입력 : [1,3,2,3,2]<br>
결과 : 8
  
## 풀이
> 정렬을 한 뒤에 자신과 다른 무게를 가지고 있는 볼링공을 차례로 비교하여 count하면 쉽게 풀 수 있는 문제다. 하지만,
> 나는 n^2으로 풀었고 답지는 n으로 풀었다. 남아있는 볼링공의 개수와 현재 해당하는 볼링공의 무게의 개수를 곱하면 더 빠른 시간복잡도로 문제를 해결할 수 있다.
> 조합을 위와 같은 방법으로 접근 할 수 있다는 것을 새롭게 배웠다.
 
### solution1(n^2)
1. 볼링공의 무게가 담겨져 있는 배열(array)를 정렬한다.
2. A 사람이 i번째 볼링 공을 골랐을 때 B가 고를 경우의 수를 이중포문을 돌려서 체크한다.(A와 무게가 다르다면 count +1을 해준다.)
3. 이중포문을 돌릴 때 i번째 이후 공만 체크하면 되기 때문에 index와 value 두가지로 포문을 돌린다.
4. return count

### solution2(n)
1. weight_list에 무게의 종류만큼 0으로 초기화한다.
2. 볼링공의 무게가 담겨져 있는 배열을 반복문을 돌면서 볼링공의 무게에 해당하는 index에 값을 1씩 증가해준다.
3. 볼링공의 최대 무게까지 반복문을 돈다.
4. 현재 인덱스 무개의 볼링공의 개수를 전체 개수에서 제외해준다.
5. result에 현재 인덱스 무게의 볼링공 * 전체 개수를 계산하여 더해준다.
6. return result

> 조합 문제를 어떻게 접근하냐에 따라서 시간복잡도를 줄일 수 있다. 
> 앞으로도 문제를 풀 때 최대한 시간복잡도를 생각하면서 풀 수 있도록 노력해야겠다.

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