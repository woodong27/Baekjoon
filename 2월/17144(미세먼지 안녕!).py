delta=((-1,0),(1,0),(0,-1),(0,1))

R,C,T=map(int,input().split())

room=[list(map(int,input().split()))for _ in range(R)]

si1=si2=0
for i in range(R):
    if room[i][0]==-1:
        si1=i
        si2=i+1
        break

for _ in range(T):
    dusts=[]
    for i in range(R):
        for j in range(C):
            if room[i][j]!=0 and room[i][j]!=-1:
                dusts.append((i,j,room[i][j]))

    diffresult=[]
    while dusts:
        ci,cj,curdust=dusts.pop()
        cnt=0
        for di,dj in delta:
            ni,nj=ci+di,cj+dj
            if 0<=ni<R and 0<=nj<C and room[ni][nj]!=-1:
                cnt+=1
                room[ni][nj]+=curdust//5
        diffresult.append((ci,cj,-(curdust//5)*cnt))

    while diffresult:
        ci,cj,decrease=diffresult.pop()
        room[ci][cj]+=decrease

    di=[-1,0,1,0]
    dj=[0,1,0,-1]
    si,sj=si1,0
    k=0
    while True:
        if not 0<=si+di[k]<si1+1 or not 0<=sj+dj[k]<C:
            k+=1
            if k==4:
                k=0
        ni,nj=si+di[k],sj+dj[k]
        room[si][sj]=room[ni][nj]
        if si==si1 and sj==0:
            room[si][sj]=0
        si+=di[k]
        sj+=dj[k]
        if si==si1 and sj==0:
            break
    room[si1][0]=-1

    si,sj=si2,0
    k=3
    while True:
        if not si2<=si+di[k]<R or not 0<=sj+dj[k]<C:
            k-=1
            if k==-1:
                k=3
        ni,nj=si+di[k],sj+dj[k]
        room[si][sj]=room[ni][nj]
        if si==si2 and sj==0:
            room[si][sj]=0
        si+=di[k]
        sj+=dj[k]
        if si==si2 and sj==0:
            break
    room[si2][0]=-1

ans=0
for i in range(R):
    for j in range(C):
        if room[i][j]!=-1 and room[i][j]!=0:
            ans+=room[i][j]

print(ans)