N,M=map(int,input().split())
i,j,direction=map(int,input().split())

room=[list(map(int,input().split()))for _ in range(N)]

di=[-1,0,1,0] #북 동 남 서
dj=[0,1,0,-1] #0 1 2 3

ans=0
while True:
    if room[i][j]==0:
        room[i][j]=2
        ans+=1

    else:
        cnt=0
        for k in range(4):
            ni,nj=i+di[k],j+dj[k]
            if room[ni][nj]!=0:
                cnt+=1

        if cnt==4:
            if room[i-di[direction]][j-dj[direction]]==1:
                break
            else:
                i-=di[direction]
                j-=dj[direction]

        else:
            direction-=1
            if direction==-1:
                direction=3
            if room[i+di[direction]][j+dj[direction]]==0:
                i+=di[direction]
                j+=dj[direction]

print(ans)