def solution(start_year, last_year, start_day, find):
    date_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_date_list = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_dict = {
        "mon": 0,
        "tue": 1,
        "wed": 2,
        "thu": 3,
        "fri": 4,
        "sat": 5,
        "sun": 6
    }
    change_day_dict = {
        "31": 3,
        "30": 2,
        "29": 1,
        "28": 0,
        "0": 0
    }

    year = start_year
    first_day = day_dict[start_day]
    find_day = day_dict[find]

    find_count_list = []
    while year <= last_year:
        count = 0
        if year % 4 == 0 and year % 400 != 0:
            for date in leap_date_list[:-1]:
                first_day = (first_day + change_day_dict[str(date)]) % 7
                if first_day == find_day:
                    count += 1
        else:
            for date in date_list[:-1]:
                first_day = (first_day + change_day_dict[str(date)]) % 7
                if first_day == find_day:
                    count += 1
        find_count_list.append(count)
        first_day = (first_day + change_day_dict[str(date_list[-1])]) % 7
        year += 1

    return sum(find_count_list[1:])


if __name__ == "__main__":
    start_year = 1900
    last_year = 2000
    start_day = "mon"
    find = "sun"

    answer = solution(start_year, last_year, start_day, find)
    print(answer)