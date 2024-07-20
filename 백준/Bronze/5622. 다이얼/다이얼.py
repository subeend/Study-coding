alpa =['ABC', 'DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
s =input()

time = 0
for data in alpa:
    for x in data:# 입력받은 문자열 하나씩 분리
        
        for i in s:
            if i == x:
                time = time+alpa.index(data)+3

print(time)