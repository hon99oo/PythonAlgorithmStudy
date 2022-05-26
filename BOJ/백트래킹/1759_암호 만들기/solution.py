def dfs(string, depth, index, visited):
    global answer
    if depth == l:
        count = 0
        for v in visited:
            if v in collection:
                count += 1
        if 1 <= count <= l-2:
            answer.append(visited.copy())
    else:
        for i in range(index, c):
            if string[i] in visited:
                continue
            visited[depth] = string[i]
            dfs(string, depth+1, i+1, visited)
            visited[depth] = ''


def solution(string):
    string.sort()
    visited = [''] * l
    dfs(string, 0, 0, visited)


if __name__ == "__main__":
    l, c = map(int, input().split())
    string = list(map(str, input().split()))
    answer = []
    collection = {'a', 'e', 'i', 'o', 'u'}
    solution(string)
    for a in answer:
        print(''.join(a))