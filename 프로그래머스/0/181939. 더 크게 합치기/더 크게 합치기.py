def solution(a, b):
    sub1= str(a)+str(b)
    sub2= str(b)+str(a)
    if sub1>sub2:
        return int(sub1)
    else:
        return int(sub2)