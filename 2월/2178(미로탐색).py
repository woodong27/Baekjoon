from collections import deque

N,M=map(int,input().split())
maze=[list(input())for _ in range(N)]

def bfs():
    que=deque([])
    visited=[[0 for _ in range(M)]for _ in range(N)]
    que.append((0,0,1))
    while que:
        ci,cj,cnt=que.popleft()
        if ci==N-1 and cj==M-1:
            return cnt
        for k in ((-1,0),(1,0),(0,-1),(0,1)):
            if 0<=ci+k[0]<N and 0<=cj+k[1]<M:
                ni,nj=ci+k[0],cj+k[1]
                if not visited[ni][nj] and maze[ni][nj]=='1':
                    que.append((ni,nj,cnt+1))
                    visited[ni][nj]=1

print(bfs())