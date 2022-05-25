"""
Q2. Given a list of timestamps in sequential order, return a list of lists grouped by week (7 days) using the first timestamp as the starting point.

example:

ts = [
    '2019-01-01',
    '2019-01-02',
    '2019-01-08',
    '2019-02-01',
    '2019-02-02',
    '2019-02-05',
]

def weekly_aggregation(ts) -> [
    ['2019-01-01', '2019-01-02'],
    ['2019-01-08'],
    ['2019-02-01', '2019-02-02'],
    ['2019-02-05'],
]
"""

def solution(ts):
    month_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    length = len(ts)
    answer = []
    store = []
    store.append(ts[0])
    for i in range(1, length):
        month = ts[i][5:7]
        day = ts[i][8:]
        if month == "01":
            date = int(day)
        else:
            sum(month_list[int(month)])

        day = ts[i][8:]



if __name__ == "__main__":
    ts = [
        '2019-01-01',
        '2019-01-02',
        '2019-01-08',
        '2019-02-01',
        '2019-02-02',
        '2019-02-05',
    ]
    solution(ts)
