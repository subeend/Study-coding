A,B,V = map(int, input().split())

V-=A
day = (V//(A-B)) + 1

if V%(A-B)==0:
    print(day)
else:
    print(day+1)