N,M = map(int, input().split())
A=[]
for a in range(N):
    A.append(a+1)
    
for _ in range(M):
    i,j = map(int, input().split())
    A[i-1],A[j-1]= A[j-1],A[i-1]
  
for a in range(N):
    print(A[a])

    