N=int(input())

lst=[list(map(str,input()))for _ in range(N)]
lst_blind=[[0 for _ in range(N)]for _ in range(N)]

di=[-1,1,0,0]
dj=[0,0,-1,1]


def dfs(lst,si,sj,color):
    stack = []
    stack.append([si, sj])

    while stack:
        now = stack.pop()
        if not visited[now[0]][now[1]]:
            visited[now[0]][now[1]] = 1
            for k in range(4):
                if 0<=now[0]+di[k]<N and 0<=now[1]+dj[k]<N and lst[now[0]+di[k]][now[1]+dj[k]]==color and not visited[now[0]+di[k]][now[1]+dj[k]]:
                    stack.append([now[0]+di[k],now[1]+dj[k]])
                    lst[now[0]+di[k]][now[1]+dj[k]]=0

for i in range(N):
    for j in range(N):
        if lst[i][j]=='R' or lst[i][j]=='G':
            lst_blind[i][j]='R'
        else:
            lst_blind[i][j]=lst[i][j]

visited=[[0 for _ in range(N)]for _ in range(N)]

cnt=0
for i in range(N):
    for j in range(N):
        if lst[i][j]=='R':
            si,sj=i,j
            dfs(lst,si,sj,'R')
            cnt+=1
        elif lst[i][j]=='G':
            si,sj=i,j
            dfs(lst,si,sj,'G')
            cnt+=1
        elif lst[i][j]=='B':
            si,sj=i,j
            dfs(lst,si,sj,'B')
            cnt+=1

visited=[[0 for _ in range(N)]for _ in range(N)]
cnt_b=0
for i in range(N):
    for j in range(N):
        if lst_blind[i][j]=='R':
            si,sj=i,j
            dfs(lst_blind,si,sj,'R')
            cnt_b+=1
        elif lst_blind[i][j]=='B':
            si,sj=i,j
            dfs(lst_blind,si,sj,'B')
            cnt_b+=1

print(cnt,cnt_b)