# BOJ

## 문자열 1316 그룹 단어 체커
[문제로 이동!](https://www.acmicpc.net/problem/1316)

## 문제

그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

## 예제 입력

{% highlight python %}

    """
    case 1:
    입력
    3
    happy
    new
    year
    출력
    3

    case 2:
    입력
    4
    aba
    abab
    abcabc
    a
    출력
    1
    """
{% endhighlight %}

## 풀이

이중 반복문을 사용해서 탐색하는 값부터 n까지 다시 순회 하면서 자기 자신과 다른 값을 찾게 되면 flag를 True로 바꿔주고, flag가 True이고 자기 자신과 같은 값인 조건을 만족하면 False로 리턴한다.
그렇지 않다면 True를 리턴해서 True로 리턴된 개수를 출력한다.

## 코드

{% highlight python %}

    import sys
    
    
    def solution(string):
        length = len(string)
        for i in range(length):
            flag = False
            for j in range(i+1, length):
                if string[i] != string[j]:
                    flag = True
                if string[i] == string[j] and flag:
                    return False
        return True
    
    
    if __name__ == "__main__":
        n = int(input())
        strings = [sys.stdin.readline().rstrip() for _ in range(n)]
        count = 0
        for string in strings:
            if solution(string):
                count += 1
        print(count)
{% endhighlight %}