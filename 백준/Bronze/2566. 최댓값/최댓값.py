n=0
m=0
max_num=0

for i in range(9):
    lst=list(map(int, input().split()))
    
    if max(lst)>max_num:
        n = i
        m = lst.index(max(lst))
        max_num = max(lst)
        
print(max_num)
print(n+1,m+1)