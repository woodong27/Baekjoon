lst=[[0 for x in range(100)]for x in range(100)]

T=int(input())

for x in range(T):
    left,low=map(int,input().split())

    for i in range(100-(10+low),100-low):
        for j in range(left,left+10):
            lst[i][j]+=1

count=0
for i in range(100):
    for j in range(100):
        if lst[i][j]>=1:
            count+=1

print(count)