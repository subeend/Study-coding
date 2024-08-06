def solution(a, b):
    answer = 0
    sub1=str(a)+str(b)
    sub2= str(b)+str(a)
    answer = max(sub1,sub2)
    return answer