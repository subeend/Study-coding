X = int(input())
N = int(input())
sum =0

for i in range (N):
    price, t = map(int, input().split())
    sum += (price*t)

if X == sum:
    print("Yes")
else:
    print("No")

