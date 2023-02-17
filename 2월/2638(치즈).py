N,M=map(int,input().split())
lst=[list(map(int,input().split()))for _ in range(N)]
visited=[[0 for _ in range(M)]for _ in range(N)]

from pprint import pprint

di=[-1,1,0,0]
dj=[0,0,-1,1]

melted=[]
for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
            cnt = 0
            for k in range(4):
                if lst[i+di[k]][j+dj[k]]==0:
                    cnt+=1
            if cnt>=2:
                melted.append([i,j])

ans=0
while melted:
    while melted:
        popped=melted.pop()
        lst[popped[0]][popped[1]]=0

    ans += 1

    for i in range(N):
        for j in range(M):
            if lst[i][j]==1:
                cnt=0
                for k in range(4):
                    if lst[i+di[k]][j+dj[k]]==0:
                        cnt+=1
                if cnt>=2:
                    melted.append([i,j])

print(ans)