from collections import deque

field=[list(input())for _ in range(12)]
di=[0,0,-1,1]
dj=[-1,1,0,0]

def puyo(si,sj):
    q=deque([(si,sj)])
    temp=[(si,sj)]
    while q:
        ci,cj=q.popleft()
        for k in range(4):
            ni,nj=ci+di[k],cj+dj[k]
            if 0<=ni<12 and 0<=nj<6 and field[si][sj]==field[ni][nj]:
                if (ni,nj) not in temp:
                    q.append((ni,nj))
                    temp.append((ni,nj))

    if len(temp)>=4:
        field[i][j]='s'
        exp.extend(temp)
        while temp:
            chi,chj=temp.pop()
            field[chi][chj]='s'

cnt=0
while True:
    exp=[]
    for i in range(11,0,-1):
        for j in range(6):
            if field[i][j]!='.' and field[i][j]!='s':
                puyo(i,j)

    if not exp:
        break

    exp.sort(key=lambda x:x[0],reverse=True)
    while exp:
        ci,cj=exp.pop()
        for ii in range(ci,0,-1):
            field[ii][cj]=field[ii-1][cj]
            if ii==1:
                field[ii-1][cj]='.'
    cnt+=1

print(cnt)