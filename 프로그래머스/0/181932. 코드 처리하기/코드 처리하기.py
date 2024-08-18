def solution(code):
    answer=''
    
    mode = False
    for idx,i in enumerate(code):
        if i =="1":
            mode = not mode
            continue
        if not mode and idx%2==0:
            answer += i
        elif mode and idx%2==1:
            answer += i
    if not answer:
        return "EMPTY"
    
    return answer