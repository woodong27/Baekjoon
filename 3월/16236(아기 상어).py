from collections import deque

N=int(input())
sea=[list(map(int,input().split()))for _ in range(N)]

di=[-1,1,0,0]
dj=[0,0,-1,1]

si=sj=0
for i in range(N):
    for j in range(N):
        if sea[i][j]==9:
            si,sj=i,j
            sea[i][j]=0

def findeatable(i,j):
    visited=[[0]*N for _ in range(N)]
    lst=[]
    q=deque([(i,j,0)])
    visited[i][j]=1
    while q:
        ci,cj,cnt=q.popleft()
        for k in range(4):
            ni,nj=ci+di[k],cj+dj[k]
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and sea[ni][nj]<=size:
                q.append((ni,nj,cnt+1))
                visited[ni][nj]=1
                if 1<=sea[ni][nj]<size:
                    lst.append((ni,nj,cnt+1))

    lst.sort(key=lambda x:(-x[2],-x[0],-x[1]))
    return lst

from pprint import pprint
ans=0
size=2
growcnt=0
eatable=findeatable(si,sj)
while eatable:
    visit=[[0]*N for _ in range(N)]
    gi,gj,distance=eatable.pop()
    q=deque([(si,sj,0)])
    visit[si][sj]=1
    while q:
        ci,cj,cnt=q.popleft()
        if ci==gi and cj==gj:
            print(ci,cj)
            ans+=cnt
            sea[ci][cj]=0
            pprint(sea)
            si,sj=ci,cj
            growcnt+=1
            if growcnt==size:
                size+=1
                growcnt=0
                eatable=findeatable(si,sj)
            break
        else:
            for k in range(4):
                ni,nj=ci+di[k],cj+dj[k]
                if 0<=ni<N and 0<=nj<N and not visit[ni][nj] and sea[ni][nj]<=size:
                    q.append((ni,nj,cnt+1))
                    visit[ni][nj]=1

print(ans)