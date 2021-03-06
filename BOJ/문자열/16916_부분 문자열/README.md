# BOJ

## 수학 16916 부분 문자열
[문제로 이동!](https://www.acmicpc.net/problem/16916)

## 문제

문자열 S의 부분 문자열이란, 문자열의 연속된 일부를 의미한다.

예를 들어, "aek", "joo", "ekj"는 "baekjoon"의 부분 문자열이고, "bak", "p", "oone"는 부분 문자열이 아니다.

문자열 S와 P가 주어졌을 때, P가 S의 부분 문자열인지 아닌지 알아보자.

## 입력

첫째 줄에 문자열 S, 둘째 줄에 문자열 P가 주어진다. 두 문자열은 빈 문자열이 아니며, 길이는 100만을 넘지 않는다. 또, 알파벳 소문자로만 이루어져 있다.

## 예제 입력

{% highlight python %}

    """
    case 1:
    입력    
    baekjoon
    aek
    출력
    1

    case 2:
    입력
    baekjoon
    oone
    출력
    0
    """
{% endhighlight %}

## 풀이

완전탐색을 사용해서 문제를 풀게되면 시간초과로 인해 정답을 도출해내지 못한다. 이럴 경우에 문자열의 부분 문자열을 탐색할 수 있는 KMP 알고리즘을 사용하면 된다. KMP 알고리즘은 패턴에 해당되는 문자열의 접두사와 접미사를 조사한 pi 배열을 이용해서
중복되는 부분을 중복 없이 탐색할 수 있도록 도와주는 알고리즘이다.

[자세한 KMP 설명으로!](https://devbull.xyz/python-kmp-algorijeumeuro-munjayeol-cajgi/)
- 위 블로그 글이 굉장히 도움이 많이 되었다.

## 코드

{% highlight python %}
    
    import sys
    
    
    def KMPSearch(pat, txt):
        M = len(pat)
        N = len(txt)
    
        lps = [0]*M
    
        computeLPS(pat, lps)
    
        i = 0
        j = 0
        while i < N:
            if pat[j] == txt[i]:
                i += 1
                j += 1
            elif pat[j] != txt[i]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
    
            if j == M:
                return 1
        return 0
    
    
    def computeLPS(pat, lps):
        leng = 0
    
        i = 1
        while i < len(pat):
            if pat[i] == pat[leng]:
                leng += 1
                lps[i] = leng
                i += 1
            else:
                if leng != 0:
                    leng = lps[leng-1]
                else:
                    lps[i] = 0
                    i += 1
    
    
    if __name__ == "__main__":
        txt = sys.stdin.readline().rstrip()
        pat = sys.stdin.readline().rstrip()
        print(KMPSearch(pat, txt))
{% endhighlight %}