from collections import deque

n,m=map(int,input().split())
block=[[0]*(n+1)for _ in range(m+1)]

num=int(input())
for i in range(num+1):
    cardinal,distance=map(int,input().split())

    if cardinal==1:
        if i==num:
            si,sj=0,distance
        else:
            block[0][distance]=i+1
    elif cardinal==2:
        if i == num:
            si,sj=m,distance
        else:
            block[m][distance]=i+1
    elif cardinal==3:
        if i==num:
            si,sj=distance,0
        else:
            block[distance][0]=i+1
    else:
        if i==num:
            si,sj=distance,n
        else:
            block[distance][n]=i+1

delta=((-1,0),(1,0),(0,1),(0,-1))
visited=[[0]*(n+1)for _ in range(m+1)]
for i in range(1,m):
    for j in range(1,n):
        visited[i][j]=1

q=deque([(si,sj)])
visited[si][sj]=1
ans=0
while q:
    ci,cj=q.popleft()
    if block[ci][cj]!=0:
        ans+=visited[ci][cj]-1
        block[ci][cj]=0

    for di,dj in delta:
        ni,nj=ci+di,cj+dj
        if 0<=ni<m+1 and 0<=nj<n+1 and not visited[ni][nj]:
            visited[ni][nj]=visited[ci][cj]+1
            q.append((ni,nj))

print(ans)
