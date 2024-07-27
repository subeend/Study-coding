n = int(input())
x, y = [], []
for i in range(n):
    a, b= map(int, input().split())
    x.append(a)
    y.append(b)

x1 = max(x) - min(x)
y1 = max(y) - min(y)
print(x1 * y1)