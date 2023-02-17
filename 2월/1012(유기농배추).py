T=int(input())

di=[-1,1,0,0]
dj=[0,0,-1,1]

def dfs(si,sj):
    stack=[]
    stack.append([si,sj])

    while stack:
        now=stack.pop()
        if not visited[now[0]][now[1]]:
            visited[now[0]][now[1]]=1
            for k in range(4):
                if 0<=now[0]+di[k]<N and 0<=now[1]+dj[k]<M and not visited[now[0]+di[k]][now[1]+dj[k]]:
                    stack.append([now[0]+di[k],now[1]+dj[k]])
                    field[now[0]+di[k]][now[1]+dj[k]]=0


for tc in range(T):
    M,N,K=map(int,input().split())

    field=[[0 for _ in range(M)]for _ in range(N)]

    for i in range(K):
        x,y=map(int,input().split())
        field[y][x]=1

    visited=[[0 for _ in range(M)]for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if field[i][j]==0:
                visited[i][j]=1

    cnt=0
    for i in range(N):
        for j in range(M):
            if field[i][j]==1:
                dfs(i,j)
                cnt+=1

    print(cnt)