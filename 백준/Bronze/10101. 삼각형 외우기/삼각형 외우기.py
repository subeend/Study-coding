x=int(input())
y=int(input())
z=int(input())
if x+y+z==180:
    if x==60 and y==60 and z==60:
        print("Equilateral")
    elif x==y or x==z or z==y:
        print("Isosceles")
    elif x!=y and y!=z:
        print("Scalene")
else:
    print("Error")