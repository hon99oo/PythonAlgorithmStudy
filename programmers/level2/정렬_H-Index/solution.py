def solution(citations):
    answer_list = []

    for citation in range(max(citations)+1):
        citations_up = 0
        citations_down = 0
        for compare in citations:
            if citation<=compare:
                citations_up+=1
            else:
                citations_down+=1
        if citations_up >= citation and citations_down <= citation:
            answer_list.append(citation)
    answer = max(answer_list)
    return answer

if __name__ == "__main__":
    citations = [3, 0, 6, 1, 5]
    print(solution(citations))