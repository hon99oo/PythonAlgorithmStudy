# BOJ

## 그리디 2138 전구와 스위치
[문제로 이동!](https://www.acmicpc.net/problem/2138)

## 문제

N개의 스위치와 N개의 전구가 있다. 각각의 전구는 켜져 있는 상태와 꺼져 있는 상태 중 하나의 상태를 가진다. i(1 < i < N)번 스위치를 누르면 i-1, i, i+1의 세 개의 전구의 상태가 바뀐다. 즉, 꺼져 있는 전구는 켜지고, 켜져 있는 전구는 꺼지게 된다. 1번 스위치를 눌렀을 경우에는 1, 2번 전구의 상태가 바뀌고, N번 스위치를 눌렀을 경우에는 N-1, N번 전구의 상태가 바뀐다.

N개의 전구들의 현재 상태와 우리가 만들고자 하는 상태가 주어졌을 때, 그 상태를 만들기 위해 스위치를 최소 몇 번 누르면 되는지 알아내는 프로그램을 작성하시오.

## 입력

첫째 줄에 자연수 N(2 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 전구들의 현재 상태를 나타내는 숫자 N개가 공백 없이 주어진다. 그 다음 줄에는 우리가 만들고자 하는 전구들의 상태를 나타내는 숫자 N개가 공백 없이 주어진다. 0은 켜져 있는 상태, 1은 꺼져 있는 상태를 의미한다.

## 예제 입력
{% highlight python %}

    """
    case 1:
    입력
    3
    000
    010
    출력
    3

    case 2:
    입력
    7   
    1101000
    1111111
    출력
    3

    case 3:
    입력    
    8
    00000000
    11011000
    출력
    2
    """
{% endhighlight %}

## 풀이
> 진짜 어려웠던 문제다... 전구를 키는 방법이 여러가지인데 어떻게 최소값을 찾는지 정말 아이디어가 떠오르지 않았다. 하지만, 이번 문제를 해결하고 또 이전에 이 문제와 비슷한 문제를 겪어 봤을 때
> 결론은, <strong>최소값을 구할 때 어떻게 해야지 최소값이 나오는지 모를 때는 앞에서부터 차근차근 계산해 나가는 방법</strong>으로 접근 해봐야 한다. 하지만 이 문제는 
> 양 끝을 키고 끌 때 다르게 작동된다. 그렇기 때문에 첫번째 전구를 킨 case와 키지 않은 case 두가지 case로 나누어 풀어야한다. 또한 마지막 테케가 계속 틀렸는데, 입렵값이 애초부터
> 같은 값인 것을 예외처리 해주어야 한다.

### solution
1. change 함수를 정의해 준다. 0이면 1, 1이면 0, 양 끝이 변경 될 때의 조건을 포함한다.
2. 입력값 두개가 서로 같으면 0으로 얼리 리턴 해준다.
3. 전구를 누르는 로직은 현재 조사하는 위치의 왼쪽 전구(즉, 다음 전구를 조사하게 되면 해당 전구는 더이상 키거나 끌 수 없는 전구)가 결과 값과 다르다면 현재 위치의 전구를 누른다.
4. 위의 로직을 첫번째 전구를 눌렀을 경우, 누르지 않았을 경우 두가지로 나누어 처리한다.
5. 계산이 끝나면, 각 경우의 결과값중 최소값을 리턴하면 되지만, 정답을 도출할 수 없는 경우 count가 -1로 저장되기 때문에 해당 부분에 적절한 분기 처리를 해준다.

## 코드

{% highlight python %}

    import sys
    
    
    def change(first, i, n):
        if i != 0:
            if first[i - 1] == "0":
                first[i - 1] = "1"
            else:
                first[i - 1] = "0"
        if first[i] == "0":
            first[i] = "1"
        else:
            first[i] = "0"
        if i != n - 1:
            if first[i + 1] == "0":
                first[i + 1] = "1"
            else:
                first[i + 1] = "0"
    
    
    def solution(n, first, last):
        if first == last:
            return 0
    
        first_f = list(first)
        first_n = list(first)
        last = list(last)
        count_f, count_n = -1, -1
    
        # 첫 번째 전구를 누르는 경우
        change(first_f, 0, n)
        count = 0
        for i in range(1,n):
            if first_f[i-1] != last[i-1]:
                change(first_f, i, n)
                count += 1
        if first_f == last:
            count_f = count+1
    
        # 첫 번째 전구를 누르지 않을 경우
        count = 0
        for i in range(1,n):
            if first_n[i-1] != last[i-1]:
                change(first_n, i, n)
                count += 1
        if first_n == last:
            count_n = count
    
        if count_n == -1 and count_f != -1:
            return count_f
        elif count_n != -1 and count_f == -1:
            return count_n
        elif count_n != -1 and count_f != -1:
            return min(count_f, count_n)
        else:
            return -1
    
    
    if __name__ == "__main__":
        n = int(input())
        first = sys.stdin.readline().rstrip()
        last = sys.stdin.readline().rstrip()
        print(solution(n, first, last))
{% endhighlight %}