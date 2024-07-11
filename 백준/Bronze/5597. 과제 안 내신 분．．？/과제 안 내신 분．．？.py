

A=[ i for i in range(1,31)]

for _ in range(28):
    n = int(input())
    A.remove(n)
    
print(min(A))
print(max(A))