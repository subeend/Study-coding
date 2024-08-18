def solution(numLog):
    answer = ''
    key = dict(zip([1, -1, 10, -10], ['w', 's', 'd', 'a']))
    for i in range(1, len(numLog)):
        answer += key[numLog[i] - numLog[i-1]] # 해당 key에 해당하는 value 값을 가져오기 
    return answer
