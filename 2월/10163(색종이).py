N=int(input())

plane=[[0 for _ in range(1001)]for _ in range(1001)]

for n in range(N):
    sj,si,width,height=map(int,input().split())

    for i in range(si,si+height):
        for j in range(sj,sj+width):
            plane[i][j]=n+1

result=[0 for _ in range(N)]
for n in range(N):
    for i in range(1001):
        for j in range(1001):
            if plane[i][j]==n+1:
                result[n]+=1

for i in range(N):
    print(result[i])