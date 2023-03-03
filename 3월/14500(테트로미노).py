N,M=map(int,input().split())

paper=[list(map(int,input().split()))for _ in range(N)]

tet1=[[0,0],[0,1],[0,2],[0,3]]
tet2=[[0,0],[0,1],[1,0],[1,1]]
tet3=[[0,0],[1,0],[2,0],[2,1]]
tet4=[[0,0],[1,0],[1,1],[2,1]]
tet5=[[0,0],[0,1],[0,2],[1,1]]

def rotate(tet):
    for k in range(4):
        tet[k][0],tet[k][1]=-tet[k][1],tet[k][0]

    return tet

def detect(si,sj,tet):
    result=[0]

    cnt1=temp1=0
    for k in range(4):
        ni,nj=si+tet[k][0],sj+tet[k][1]
        if 0<=ni<N and 0<=nj<M:
            cnt1+=1
            temp1+=paper[ni][nj]

    if cnt1>=4:
        result.append(temp1)

    cnt2=temp2=0
    for k in range(4):
        ni,nj=si+tet[k][1],sj+tet[k][0]
        if 0<=ni<N and 0<=nj<M:
            cnt2+=1
            temp2+=paper[ni][nj]

    if cnt2>=4:
        result.append(temp2)

    return max(result)


ans=0
for i in range(N):
    for j in range(M):
        a=detect(i,j,tet1)
        b=detect(i,j,tet2)
        c=detect(i,j,tet3)
        d=detect(i,j,tet4)
        e=detect(i,j,tet5)

        temp3=[]
        for _ in range(3):
            rtet3=rotate(tet3)
            temp3.append(detect(i,j,rtet3))

        temp4=[]
        for _ in range(3):
            rtet4=rotate(tet4)
            temp4.append(detect(i,j,rtet4))

        temp5=[]
        for _ in range(3):
            rtet5=rotate(tet5)
            temp5.append(detect(i,j,rtet5))

        ans=max(ans,a,b,c,d,e,max(temp3),max(temp4),max(temp5))

print(ans)