x,y,w,h=map(int,input().split())
print(min(x,y,w-x,h-y)) # 영역안에서 최소를 골라주면됨 