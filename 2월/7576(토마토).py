from collections import deque

m,n=map(int,input().split())
box=[list(map(int,input().split()))for _ in range(n)]
visited=[[0 for _ in range(m)]for _ in range(n)]

di=[-1,1,0,0]
dj=[0,0,-1,1]

def bfs(point):
    que=deque([])
    que.extend(point)
    global cnt
    while que:
        ci,cj,cnt=que.popleft()
        visited[ci][cj]=1
        for k in range(4):
            if 0<=ci+di[k]<n and 0<=cj+dj[k]<m:
                ni,nj=ci+di[k],cj+dj[k]
                if not visited[ni][nj] and box[ni][nj]==0:
                    que.append((ni,nj,cnt+1))
                    box[ni][nj]=1
                    visited[ni][nj]=1

bfspoint=[]
for i in range(n):
    for j in range(m):
        if box[i][j]==1:
            bfspoint.append((i,j,0))

cnt=0
bfs(bfspoint)

ans=cnt
for i in box:
    if 0 in i:
        ans=-1
        break

print(ans)