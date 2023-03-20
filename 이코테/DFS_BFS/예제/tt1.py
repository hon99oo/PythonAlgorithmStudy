import random


def cal_fitness(generation):
    """
    적합도 함수
    현재 세대의 chromosome 값들을 인자로 받아들여 적합도 함수를 계산
    return: 각 chromosome 의 적합도 값을 저장한 배열로 리턴
    """
    # 적합도 함수의 계산값을 미리 정의
    fitness_value = [10, 20, 50, 100, 70, 40, 90]
    fitness = []

    # 반복문을 돌며 fitness_value에서 값을 하나씩 꺼내 chromosome 값을 계산
    for x in generation:
        sum_v = 0
        for i, v in enumerate(x):
            sum_v += (v - fitness_value[i]) ** 2
        # 계산된 적합도를 fitness 배열에 저장
        fitness.append(sum_v)

    return fitness


def extract_low_fitness(generation, length):
    """
    적합도 값이 가장 낮은 4개의 chromosome을 뽑기 위한 함수
    return: length개의 가장 낮은 적합도 값의 chromosome이 저장된 배열로 리턴
    """
    # 적합도 함수 호출
    fitness = cal_fitness(generation)
    # 적합도 값과 chromosome을 tuple 형식으로 재정의
    tmp = [(generation[i], fitness[i]) for i in range(20)]
    # 적합도 값을 기준으로 오름차순 정렬
    tmp.sort(key=lambda x: x[1])
    # 상위 length개의 튜플에서 chromosome 값만을 best_fitness 배열에 저장
    best_fitness = [x[0] for x in tmp[:length]]
    return best_fitness


def selection(generation):
    """
    selection 함수
    적합도 함수값을 계산하고, 룰렛팅을 실행하여 값을 저장하고 chromosome의 채택 확률이 랜덤한 값보다 작거나 같으면 해당 chromosome을 저장한다.
    return: selection을 적용한 연속된 새로운 chromosome이 포함된 generation
    """
    # 적합도 함수 호출
    fitness = cal_fitness(generation)
    # 적합도 값이 저장된 배열을 내림차순으로 정렬
    fitness.sort(reverse=True)
    # rank를 설정하기 위해 첫번째 값을 queue에 append
    queue = [fitness[0]]
    # 첫번째 값을 rank 1로 설정
    rank = [1]
    # 반복문을 돌며 현재 queue의 값과 같다면, 해당 값의 rank와 같은 값으로 rank 설정, 같지 않다면 rank+1로 설정
    for i in range(1,20):
        if queue[-1] == fitness[i]:
            rank.append(rank[-1])
            queue.append(fitness[i])
        else:
            rank.append(i+1)
            queue.append(fitness[i])
    # rank를 다시 오름차순으로 정렬
    rank.sort(reverse=True)
    # rank의 합을 계산
    rank_sum = sum(rank)
    # 누적합을 저장하기 위하여 배열을 하나 생성
    roulette_probability = []
    tmp = 0
    # 반복문을 돌며 누적합을 계산하여 roulette_probability 배열에 저장
    for x in rank:
        tmp += x/rank_sum
        roulette_probability.append(tmp)

    # 0과 1 사이의 값을 랜덤하게 생성
    rand_list = [random.random() for _ in range(20)]
    # chromosome과 누적합 사이의 관계를 나타내기 위한 positions 배열 생성
    positions = []
    # 반복문을 돌며 새로운 랜덤 값이 누적합의 어떤 위치에 있는지 탐색(누적합의 배열이 오름차순으로 정렬되어 있기 때문에 랜덤값이 누적합보다 작은지만을 확인한다.)
    for rand in rand_list:
        for i, x in enumerate(roulette_probability):
            if rand < x:
                positions.append(i)
                break
    # position 에 위치한 chromosome 값만을 현재 세대로 남기기 위해 반복문을 돌며 값을 저장
    new_generation = []
    for position in positions:
        new_generation.append(generation[position])

    return new_generation


def crossover(generation):
    """
    crossover 함수
    0과 1사이의 랜덤값(확률)과 0과 7 사이의 랜덤값(위치)을 구하여 확률 랜덤값이 0.5보다 크면 위치 랜덤값과 crossover 해준다.
    return: crossover 된 새로운 generation을 리턴
    """
    # 0과 1 사이의 확률 랜덤값 생성
    rand_list = [random.random() for _ in range(10)]
    # 0과 7 사이의 위치 랜덤값 생성
    gene_list = [random.randrange(0, 7) for _ in range(10)]
    # 반복문을 돌며 crossover 해준다.
    for i in range(10):
        # 확률 랜덤값이 0.5보다 크다면 crossover 해준다.
        if rand_list[i] > 0.5:
            # 위치 랜덤값과 현재 위치의 값을 tmp 변수를 사용하여 교환해준다.
            tmp = generation[i*2][gene_list[i]]
            generation[i*2][gene_list[i]] = generation[i*2+1][gene_list[i]]
            generation[i*2+1][gene_list[i]] = tmp

    return generation


def mutation(generation):
    """
    mutation 함수
    0과 1사이의 랜덤값(확률)과 0과 7 사이의 랜덤값(위치)을 구하여 확률 랜덤값이 0.3보다 작으면 위치 랜덤값을 mutation 해준다.
    return: mutation 된 새로운 generation을 리턴
    """
    # 0과 1 사이의 확률 랜덤값 생성
    rand_list = [random.random() for _ in range(20)]
    # 0과 7 사이의 위치 랜덤값 생성
    gene_list = [random.randrange(0, 7) for _ in range(20)]
    # 반복문을 돌며 mutation 해준다.
    for i in range(20):
        # 확률 랜덤값이 0.3보다 작으면 mutation 해준다.
        if rand_list[i] < 0.3:
            # 위치 랜덤값의 위치의 값을 1과 100사이의 랜덤값으로 변이시켜준다.
            generation[i][gene_list[i]] = random.randrange(1,100)

    return generation


def find_best_fitness(generation):
    """
    현재 세대에서 가장 낮은 적합도를 갖는 chromosome을 탐색하는 함수
    return: 가장 낮은 적합도를 갖는 chromosome을 리턴
    """
    # 적합도 함수 호출
    fitness = cal_fitness(generation)
    # 적합도와 chromosome을 tuple 형식으로 재정의
    tmp = [(generation[i], fitness[i]) for i in range(20)]
    # 위의 tuple을 적합도 기준으로 오름차순으로 정렬한다.
    tmp.sort(key=lambda x: x[1])
    # 가장 낮은 적합도를 갖는 chromosome인 첫번째 인덱스 값 tmp[0]을 리턴한다.
    return tmp[0]


if __name__ == "__main__":
    # 1nd generation 구성
    generation = [[random.randrange(1, 100) for _ in range(7)] for i in range(20)]

    # generation 구성을 1000번 반복하기 위해 cnt값을 0으로 초기화
    cnt = 0

    # generation 구성을 1000번 반복
    while cnt<1000:
        # 최적 적합도가 0이라면 반복문 종료
        if best_fitness[1] == 0:
            break

        # selection 함수 호출
        generation = selection(generation)
        # selection 적용 이후 적합도 값이 가장 낮은 chromosome 4개를 선택하는 함수 호출
        best_selection = extract_low_fitness(generation,4)
        # crossover 함수 호출
        generation = crossover(generation)
        # crossover 적용 이후 적합도 값이 가장 낮은 chromosome 4개를 선택하는 함수 호출
        best_crossover = extract_low_fitness(generation,4)
        # mutation 함수 호출
        generation = mutation(generation)
        # mutation 적용 이후 적합도 값이 가장 낮은 chromosome 2개를 선택하는 함수 호출
        best_mutation = extract_low_fitness(generation,2)
        # best chromosome 선택
        best_fitness = find_best_fitness(generation)
        cnt += 1

        # best chromosome과 해당 적합도 출력
        print(f"{cnt}세대: best_chromo: {best_fitness[0]}, 최적 적합도: {best_fitness[1]}")

        # 랜덤한 chromosome 10개를 생성한 후 best selection, best crossover, best mutation 값과 추가 하여 다음 세대를 구성
        generation = best_selection+best_crossover+best_mutation+[[random.randrange(1, 100) for _ in range(7)] for i in range(10)]


