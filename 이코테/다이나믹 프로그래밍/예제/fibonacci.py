import time

def fibo(x):
    if x==1 or x==2:
        return 1

    return fibo(x-1) + fibo(x-2)

d = [0] * 100

def fibo_memorization(x):
    if x==1 or x==2:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = fibo_memorization(x-1) + fibo_memorization(x-2)
    return d[x]

def fibo_memorization_bottom_up(x):
    d2 = [0] * 100
    d[1] = 1
    d[2] = 1

    for i in range(3, x+1):
        d[i] = d[i-1] + d[i-2]

    return d[x]

if __name__ == "__main__":
    print(fibo(20))
    print(fibo_memorization(20))
    print(fibo_memorization_bottom_up(20))