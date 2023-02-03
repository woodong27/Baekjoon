from pprint import pprint

N,M=map(int,input().split()) #NxM 2차원 리스트
board=[0 for x in range(N)]
temp=[[0 for x in range(8)]for x in range(8)]

for i in range(N):
    board[i]=list(input())

pprint(board)

for i in range(N):
    for j in range(M):
        if board[i][j]=='B':
            board[i][j]==0
        else:
            board[i][j]==1

pprint(board)

# for i in range(8-M+1):
#     for j in range(8):
#         temp[j]=board[j][i:8]
#
#     pprint(temp)


