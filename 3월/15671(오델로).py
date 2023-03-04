board=[['.']*6 for _ in range(6)]
board[2][2]=board[3][3]='W'
board[2][3]=board[3][2]='B'

delta=((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1))

N=int(input())
for log in range(N):
    ti,tj=map(int,input().split())
    i,j=ti-1,tj-1

    color='B'
    if log%2:
        color='W'
    board[i][j]=color

    for di,dj in delta:
        temp=[]
        for m in range(1,6):
            ni,nj=i+di*m,j+dj*m
            if 0<=ni<6 and 0<=nj<6:
                if board[ni][nj]=='.':
                    break
                elif board[ni][nj]!=color:
                    temp.append((ni,nj))
                else:
                    while temp:
                        chi,chj=temp.pop()
                        board[chi][chj]=color
                    break

cntw,cntb=0,0
for col in board:
    cntw+=col.count('W')
    cntb+=col.count('B')

win='Black'
if cntw>cntb:
    win='White'

for col in board:
    print(''.join(col))
print(win)