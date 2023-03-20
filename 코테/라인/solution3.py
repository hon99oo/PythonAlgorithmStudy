import math


def solution(fuel, powers, distances):
    length = len(powers)
    compare_list = []
    times = []
    fuel_list = [1] * length
    index = 0

    for i in range(length):
        t = distances[i]/powers[i]
        compare_list.append(t)
        times.append(t+0.5)
    fuel -= length

    while fuel > 0:
        index = times.index(max(times))
        fuel_list[index] += 1
        times[index] = compare_list[index]/fuel_list[index] + fuel_list[index]/2
        fuel -= 1

    return math.ceil(max(times))


if __name__ == "__main__":
    fuel = 19
    powers = [40, 30, 20, 10]
    distances = [1000, 2000, 3000, 4000]
    print(solution(fuel, powers, distances))
