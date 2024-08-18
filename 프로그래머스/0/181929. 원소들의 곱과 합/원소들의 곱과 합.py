def solution(num_list):
    mul=1
    sum=0
    for i in range(len(num_list)):
        mul = mul*num_list[i]
    for j in range(len(num_list)):
        sum= sum+num_list[j]
    sum=sum**2
    
    if mul>sum:
        answer = 0
    else:
        answer = 1
        
    return answer