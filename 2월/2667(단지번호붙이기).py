N=int(input())

house=[list(map(int,input()))for _ in range(N)]

di=[-1,1,0,0]
dj=[0,0,-1,1]

visited=[[0 for _ in range(N)]for _ in range(N)]

for i in range(N):
    for j in range(N):
        if house[i][j]==0:
            visited[i][j]=1

def dfs(graph,si,sj):
    stack=[]
    stack.append([si,sj])

    cnt=0
    while stack:
        now=stack.pop()
        if visited[now[0]][now[1]]==0:
            visited[now[0]][now[1]]=1
            cnt+=1
            for i in range(4):
                if 0<=now[0]+di[i]<N and 0<=now[1]+dj[i]<N:
                    ni,nj=now[0]+di[i],now[1]+dj[i]
                    if visited[ni][nj]==0 and house[ni][nj]==1:
                        stack.append([ni,nj])

    return cnt

count=[]
for i in range(N):
    for j in range(N):
        if visited[i][j]==0:
            si,sj=i,j
            count.append(dfs(house,si,sj))

count.sort()
print(len(count))
for i in range(len(count)):
    print(count[i])