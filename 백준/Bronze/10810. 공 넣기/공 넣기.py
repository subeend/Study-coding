N,M = map(int, input().split())
A=[]

for n in range(N):
    A.append(0) #A=[0]*N 
    
for _ in range(M):
    i,j,k=map(int,input().split())
    for z in range(i-1,j):
        A[z]=k
        
for a in A:
    print(a,end=" ")
    

