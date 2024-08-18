def solution(a, d, included):
    answer = 0
    seq = [a + i * d for i in range(len(included))]
    for i in range(len(included)):
        if included[i]:
            answer += seq[i]
    return answer