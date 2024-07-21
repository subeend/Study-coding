
N = int(input())


idx = 1
last_num = 1


while last_num <N:
    last_num += 6*idx
    idx += 1


print(idx)

