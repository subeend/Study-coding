N =int(input())
A=list(map(int, input().split()))

M = max(A)
for i in range(N):
    A[i]=A[i]/M*100
avg_A = sum(A)/N   
        
print(avg_A)  