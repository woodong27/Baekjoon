from collections import deque

N=int(input())
board=[[0]*N for _ in range(N)]

di=[0,1,0,-1]
dj=[1,0,-1,0]

K=int(input())
for _ in range(K):
    ai,aj=map(int,input().split())
    board[ai-1][aj-1]=1

L=int(input())
snake={}
for _ in range(L):
    time,turn=map(str,input().split())
    snake[int(time)]=turn

i,j=0,0
cnt=0
path=deque([])
k=0
while 0<=i<N and 0<=j<N:
    path.append((i,j))
    if cnt in snake.keys():
        direction=snake[cnt] #왼쪽은 k-=1, 오른쪽은 k+=1
        if direction=='L':
            k-=1
            if k==-1:
                k=3
        else:
            k+=1
            if k==4:
                k=0

    cnt+=1
    i+=di[k]
    j+=dj[k]
    if 0<=i<N and 0<=j<N and board[i][j]==1:
        board[i][j]=0
    else:
        if (i,j) in path:
            break
        else:
            path.popleft()

print(cnt)