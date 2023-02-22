from collections import deque

di=[-1,1,0,0]
dj=[0,0,-1,1]

def bfs(point):
    que=deque([])
    que.extend(point)
    while que:
        type,ci,cj,cnt=que.popleft()
        if cnt>=s:
            break
        visited[ci][cj]=1
        for k in range(4):
            if 0<=ci+di[k]<n and 0<=cj+dj[k]<n:
                ni,nj=ci+di[k],cj+dj[k]
                if not visited[ni][nj] and ttube[ni][nj]==0:
                    que.append((type,ni,nj,cnt+1))
                    ttube[ni][nj]=type

n,k=map(int,input().split())

ttube=[list(map(int,input().split()))for _ in range(n)]
s,gi,gj=map(int,input().split())
gi-=1
gj-=1

visited=[[0 for _ in range(n)]for _ in range(n)]

spoint=[]
for i in range(n):
    for j in range(n):
        if ttube[i][j]!=0:
            spoint.append((ttube[i][j],i,j,0))

spoint.sort()
# print(spoint)

bfs(spoint)
print(ttube[gi][gj])
# from pprint import pprint
# pprint(ttube,indent=1,width=15)