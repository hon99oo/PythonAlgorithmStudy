# 이코테

## 그리디 모험가 길드(Python)

## 문제

모험가 N명에겐 공포도 X가 각각 존재한다.<br>
공포도가 X인 모험가는 반드시 X명 이상으로 구성된 그룹에 참여하고 여행을 떠나야 한다.<br>
여행을 떠날 수 있는 그룹 수의 최댓값을 구하라.

- 예시<br>

입력 : [2,3,1,2,2]<br>
결과 : 5

## 풀이
> 공포도가 가장 큰 모험가를 우선으로 그룹을 지정해주어야 한다. 그렇기 때문에 내림차순으로 정렬을 하고 접근한다.

1. array를 내림차순으로 정렬
2. array의 첫번째 인덱스의 값만큼 slicing해서 array에 저장, count를 1 올려줌
3. array가 빈 리스트가 되면 while문 탈출
4. return count

## 코드

{% highlight python %}

    def solution(array):
        count = 0
        array.sort(reverse=True)
        while array:
            array = array[array[0]:]
            count += 1
    
        return count
    
    if __name__ == "__main__":
        array = [2,3,1,2,2]
        print(solution(array))

{% endhighlight %}