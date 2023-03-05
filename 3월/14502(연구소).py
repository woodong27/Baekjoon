from collections import deque
from pprint import pprint

N,M=map(int,input().split())
lab=[list(map(int,input().split()))for _ in range(N)]
delta=((0,-1),(0,1),(1,0),(-1,0))

pprint(lab)

virus=[]
for i in range(N):
    for j in range(M):
        if lab[i][j]==2:
            virus.append((i,j))

print(virus)

def diffusion():
    visited=[[0]*M for _ in range(N)]
    q=deque([])
    q.extend(virus)
    while q:
        ci,cj=q.popleft()
        for di,dj in delta:
            ni,nj=ci+di,cj+dj
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and lab[ni][nj]==0:
                q.append((ni,nj))
                visited[ni][nj]=1
                lab[ni][nj]=2

diffusion()
pprint(lab)