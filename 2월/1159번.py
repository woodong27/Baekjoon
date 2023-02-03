N=int(input())
l=[]
for i in range(N):
    l.append(input())

result=[]

for i in range(ord('a'),ord('z')+1):
    count = 0
    for j in range(len(l)):
        if chr(i)==l[j][0]:
            count+=1
            if chr(i) not in result and count==5:
                result.append(chr(i))

result=sorted(result)

if result==[]:
    print('PREDAJA')
else:
    for i in range(len(result)):
        print(result[i],end='')