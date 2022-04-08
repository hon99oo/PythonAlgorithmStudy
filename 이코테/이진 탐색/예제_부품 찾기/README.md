# 이코테

## 이진탐색 부품 찾기(Python)

## 문제

전자 매장에는 부품이 N개 있다. <br>
어느날 손님이 M개 종류의 부품을 구매하려고 한다. <br>
이 때 매장에서 손님이 사려고 하는 부품이 있는지 yes와 no 형태로 구하라.

- 예시<br>
입력 : 
        array = [9, 3, 7, 9, 2] <br>
        target = [5, 7, 9] <br>
결과 : no yes yes

## 풀이
> 탐색시간을 줄이기 위해서는 array를 정렬하고 이진 탐색으로 target에 저장된 배열의 인자를 하나씩 탐색해나가면 쉽게 풀 수 있다.

1. array를 내림차순으로 정렬
2. target 배열의 인자를 하나씩 꺼내서 target으로 설정
3. array의 end가 start보다 크거나 같을 동안 while문 반복
4. 이진탐색 알고리즘을 사용하여 탐색이 완료되면 Yes, 탐색이 되지 않으면 while 문 밖에서 No(No 저장 때 array[mid]가 t가 아닐 때의 조건을 걸어 둔 이유는 무차별적으로 No가 저장되는 것을 방지하기 위함)


## 다른 풀이
> 이진탐색 뿐만 아니라, count sorting, set 자료형을 사용하여 풀 수 있다.
> set 자료형은 {} <- 로 array를 묶어 target in {} 문법을 사용하여 쉽게 풀 수 있다.

## 코드

{% highlight python %}

    def solution(array, target, start, end):
        array.sort()
        result = []
        for t in target:
            while start <= end:
                mid = (start + end) // 2
                if array[mid] == t:
                   result.append("Yes")
                   break
                elif array[mid] > t:
                    end = mid - 1
                else:
                    start = mid + 1
            if array[mid] != t:
                result.append("No")
            start = 0
            end = len(array)-1
    
        return result
    
    
    def solution2(array, target):
        def binary_search(array, target, start, end):
            while start <= end:
                mid = (start + end) //2
                if array[mid] == target:
                    return mid
                elif array[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
    
            return None
    
        store = []
    
        for i in target:
            result = binary_search(array, i, 0, len(array)-1)
            if result != None:
                store.append("Yes")
            else:
                store.append("No")
    
        return store
    
    
    if __name__ == "__main__":
        array = [9, 3, 7, 9, 2]
        target = [5, 7, 9]
        print(solution(array, target, 0, len(array)-1))

{% endhighlight %}