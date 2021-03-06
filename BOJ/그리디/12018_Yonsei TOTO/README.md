# BOJ

## 그리디 2012 등수 매기기
[문제로 이동!](https://www.acmicpc.net/problem/12018)

## 문제

연세대학교 수강신청이 얼마 전부터 바뀌어, 마일리지 제도로 바뀌었다. 이 제도는 각각의 학생들에게 마일리지를 주어 듣고 싶은 과목에 마일리지를 과목당 1~36을 분배한다. 그리고 모두 분배가 끝이 나면 과목에 대해서 마일리지를 많이 투자한 순으로 그 과목의 수강인원만큼 신청되는 방식이다.

성준이는 연세대학교 재학 중인 학생이다. 성준이는 저번 수강신청에서 실패하여 휴학을 했기 때문에 이번 수강신청만은 필사적으로 성공하려고 한다. 그래서 성준이는 학교 홈페이지를 뚫어버렸다.

그 덕분에 다른 사람들이 신청한 마일리지를 볼 수 있게 되었다. 성준이는 주어진 마일리지로 최대한 많은 과목을 신청하고 싶어 한다. (내가 마일리지를 넣고 이후에 과목을 신청하는 사람은 없다) 마일리지는 한 과목에 1에서 36까지 넣을 수 있다.

## 입력

첫째 줄에는 과목 수 n (1 ≤ n ≤ 100)과 주어진 마일리지 m (1 ≤ m ≤ 100)이 주어진다. 각 과목마다 2줄의 입력이 주어지는데 첫째 줄에는 각 과목에 신청한 사람 수 Pi과 과목의 수강인원 Li이 주어지고 그 다음 줄에는 각 사람이 마일리지를 얼마나 넣었는지 주어진다. (1 ≤ Pi ≤100, 1 ≤ Li ≤ 100)

(단 마일리지가 같다면 성준이에게 우선순위가 주어진다고 하자.)

## 예제 입력

{% highlight python %}

    """
    입력
    5 76
    5 4 
    36 25 1 36 36
    4 4
    30 24 25 20
    6 4
    36 36 36 36 36 36
    2 4
    3 7
    5 4
    27 15 26 8 14
    
    출력
    4
    """

{% endhighlight %}

## 풀이
> 여러가지 요소들을 입력받고 어떻게 효율적으로 저장할지 고민을 좀 했던 문제이다. 수강신청 인원과 정원 그리고 학생들이 배팅한 마일리지를 하나의 set으로 묶어서 처리했고, 
> 수강신청 인원과 정원 수를 비교한뒤 조건 분기로 나누었으며, 배팅한 마일리지를 정렬해서 문제를 해결했다.

### solution
1. 첫 번째 반복문은 해당 수업을 수강하기 위해서 필요한 마일리지를 mileage 리스트에 모두 저장하는 반복문이다.
2. 수강 정원과 수강 신청 인원을 비교한 뒤 각각에 mileage 리스트에 필요한 마일리지를 append 해준다.
3. mileage 리스트를 정렬해준다.(마일리지가 적게 들어가는 수업을 우선 수강하기 위해서)
4. mileage 리스트를 하나씩 꺼내서 더해가며 총 마일리지인 m보다 커지면 반복문을 탈출한다.
* 성준이의 마일리지가 우선순위가 높은걸 주의하자! ex) [36, 36, 36, 36] 이라면 성준이가 36 마일리지를 쓴다면 수강할 수 있다.

## 코드

{% highlight python %}

    def solution(n, m, course):
        mileage = []
        for i in range(n):
            if course[i][1] - course[i][0] > 0:
                mileage.append(1)
            else:
                course[i][2].sort()
                mileage.append(course[i][2][course[i][0] - course[i][1]])
    
        mileage.sort()
        sum_v = 0
        count = 0
        for v in mileage:
            if v > 36:
                continue
            sum_v += v
            if sum_v > m:
                return count
            count += 1
    
        return count
    
    
    if __name__ == "__main__":
        n, m = map(int, input().split())
        course = []
        for _ in range(n):
            register, possible = map(int, input().split())
            course.append((register, possible, list(map(int, input().split()))))
        print(solution(n, m, course))
{% endhighlight %}