N,M = map(int, input().split())
A=[i for i in range(1,N+1)]
    
for _ in range(M):
    i,j =map(int, input().split())
    temp = A[i-1:j]
    temp.reverse()
    A[i-1:j]=temp

for i in range(N):
    print(A[i], end=" ")
    
    
