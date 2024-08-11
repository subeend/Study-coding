def solution(ineq, eq, n, m):
    
    if(ineq == "<"): 
        if(eq == "="): 
            answer = int(n<=m)  
        elif(eq == "!"):
            answer = int(n<m)
            
    elif(ineq == ">"): 
        if(eq == "="): 
            answer = int(n>=m) 
        elif(eq == "!"):
            answer = int(n>m)
    
    return answer
