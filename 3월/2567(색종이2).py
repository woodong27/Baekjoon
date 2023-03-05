board = [[0]*101 for _ in range(101)]
N = int(input())
for i in range(N):
    x,y = map(int,input().split())
    for j in range(y,y+10):
        for k in range(x,x+10):
            board[j][k] = 1

di = [-1,1,0,0]
dj = [0,0,-1,1]
cnt = 0
for i in range(100):
    for j in range(100):
        if board[i][j]==1:
            for k in range(4):
                ni,nj=i+di[k],j+dj[k]
                if 0<=ni<101 and 0<=nj<101 and board[ni][nj]==0:
                    cnt+=1

print(cnt)