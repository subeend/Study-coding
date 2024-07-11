A =[]

for i in range(10):
    n=int(input())
    if n%42 not in A:
        A.append(n%42)
   
  
print(len(A))
