# 이코테

## 그리디 무지의 먹방 라이브 - 2019 카카오 문제(Python)

## 문제

[문제로 이동!](https://programmers.co.kr/learn/courses/30/lessons/42891#qna)
  
## 풀이
> k만큼 반복문을 돌며 0을 만나면 패스하고 0이 아닌 값을 만나면 인자와 k값을 -1씩 하는 방식으로 처음 문제를 접근했다.
> index 접근은 array의 길이만큼 나눈 나머지로 접근함으로써 반복문 하나로 접근하였지만, 시간초과로 문제를 풀지 못하였다.
> 
> 답지에서는 우선순위큐로 접근하였다. 다 먹는데 가장 적게 걸리는 음식들을 순서로 접근하였고, 이 때 하나의 음식을 다 먹는 시간이 k보다 커지면 반복문을 탈출하고
> 남은 값들 중에서 정답을 도출하였다.
 
### solution2(fail)
1. k>0 인 조건에서 while문을 돈다.
2. index를 1씩 증가하고 index를 array의 length로 나눈 나머지로 배열에 접근한다.
3. 0이면 continue, 1이면 k와 인자를 -1씩 해준다.
4. 탈출 시 index로 배열에 접근하여 해당 값이 0이 아니라면 index+1(음식은 1부터 시작)로 return 한다.
5. 0일 경우 한바퀴를 돌면서 해당 index부터 순서로 0보다 큰 값을 찾는다.
6. 한바퀴가 돌아도 찾아지지 않는다면 -1로 return, 찾아졌다면 해당 index로 return

### solution3(solved)
1. array의 총합이 k보다 적으면 -1로 우선 return 하여준다.
2. (array의 값, array의 인덱스)로 값을 기준으로 정렬하여 우선순위큐에 넣어준다.
3. (현재 먹은 음식과 이전에 먹은 음식의 차이)와 (현재 배열의 길이) 를 곱하고 (이전 반복문까지 더해졌던 sum_value)와 더해서 k보다 커지면 반복문을 탈출한다.
    - 위의 값이 k보다 크다면, 더이상 음식을 다 먹을 수 있는 경우가 아니기 때문에 반복문을 탈출하고 남은 횟수만큼 인덱스를 더해 결과를 도출한다.
4. 반복문을 탈출했다면, 다시 인덱스 기준으로 정렬하고 결과값을 찾는다.

> 처음 문제를 풀었을 때 문제에서 순차적으로 접근하는 것 처럼 설명이 되어 있어 순차적으로 접근하면서 푸는 방법이 맞는 방법이라고 생각했다.
> 하지만, 문제에 대해 조금 더 생각했더라면, 우선순위큐를 생각할 수 있었을 것 같다. 다양한 유형을 풀어본다면, 어떤 유형으로 풀 수 있는 지에 대한 생각의 폭이 넓어질 것 같다.

## 새로 알게된 문법
> solution1을 풀 때 리스트 컴프리헨션의 조건문에 대한 새로운 문법을 알게 되었다.

1. 조건문이 뒤에 있을 때 : 조건문에 해당 하는 값 i만 추가

{% highlight python %}
[i for i in array if i%2 == 0]
{% endhighlight %}

2. 조건문이 앞에 있을 때 : if에 해당하는 값은 i, 아니면 else 뒤에 있는 값으로 추가
{% highlight python %}
[i if i%2 == 0 else None for i in array]
{% endhighlight %}
## 코드

{% highlight python %}

    def solution(food_times, k):
        length = len(food_times)
        quotient = k // length
        remainder = k % length
        food_times = [v-quotient-1 if i<remainder else v-quotient for i,v in enumerate(food_times)]
        time_sum = sum([i for i in food_times if i<0])
        index = (remainder + time_sum) % length
        if food_times[index] <= 0:
            for i,v in enumerate(food_times[index:]):
                if v > 0:
                    return i+index+1
            return -1
        return index
    
    
    def solution2(food_times, k):
        length = len(food_times)
        index = -1
        while k > 0:
            index += 1
            if food_times[index % length] == 0:
                continue
            else:
                food_times[index % length] -= 1
                k -= 1
    
        index = (index + 1) % length
    
        if food_times[index] <= 0:
            for i in range(length+1):
                if food_times[(index+i) % length] > 0:
                    return (index+i) % length + 1
            return -1
    
        return index+1
    
    
    def solution3(food_times, k):
        import heapq
    
        if sum(food_times) <= k:
            return -1
    
        q = []
        for i in range(len(food_times)):
            heapq.heappush(q, (food_times[i], i+1))
    
        sum_value = 0
        previous = 0
    
        length = len(food_times)
        while sum_value + ((q[0][0] - previous) * length) <= k:
            now = heapq.heappop(q)[0]
            sum_value += (now - previous) * length
            length -= 1
            previous = now
    
        result = sorted(q, key =lambda x: x[1])
        return result[(k - sum_value) % length][1]
    
    
    if __name__ == "__main__":
        food_times = [3,1,1,1,2,4,3]
        k = 12
        print(solution3(food_times,k))

{% endhighlight %}