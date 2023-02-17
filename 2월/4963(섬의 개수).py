di=[-1,1,0,0,-1,-1,1,1]
dj=[0,0,-1,1,-1,1,1,-1]

def dfs(si,sj):
    stack=[]
    stack.append([si,sj])

    while stack:
        now=stack.pop()
        if not visited[now[0]][now[1]]:
            visited[now[0]][now[1]]=1
            for k in range(8):
                if 0<=now[0]+di[k]<h and 0<=now[1]+dj[k]<w and not visited[now[0]+di[k]][now[1]+dj[k]]:
                    stack.append([now[0]+di[k],now[1]+dj[k]])
                    seamap[now[0]+di[k]][now[1]+dj[k]]=0

while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break

    seamap=[list(map(int,input().split()))for _ in range(h)]

    visited=[[0 for _ in range(w)]for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if seamap[i][j]==0:
                visited[i][j]=1

    cnt=0
    for i in range(h):
        for j in range(w):
            if seamap[i][j]==1:
                dfs(i,j)
                cnt+=1

    print(cnt)