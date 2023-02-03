N=int(input())
h,w=[],[]
for i in range(N):
    x,y=map(int,input().split())
    w.append(x)
    h.append(y)

    temp=[1]*N
    for i in range(len(w)):
        for j in range(len(w)):
            if w[i]<w[j] and h[i]<h[j]:
                temp[i]+=1

print(*temp)
