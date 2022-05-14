def solution(n, chains):
    count = 0
    chains.sort()
    use_chain = 0
    for chain in chains:
        if chain == n - 1:
            return use_chain + chain
        elif chain > n - 1:
            return use_chain + n - 1
        else:
            n -= (chain + 1)
            use_chain += chain

    return count

def solution2(n, length):
    count = 0
    length.sort()
    while len(length) > 1:
        if length[0] == 0:
            length = length[1:]
        if len(length) == 2:
            count += 1
            break
        if len(length) == 1:
            break
        length[0] -= 1
        length.append(length.pop() + length.pop())
        count += 1

    return count

if __name__ == "__main__":
    n = int(input())
    chains = list(map(int, input().split()))
    print(solution(n, chains))