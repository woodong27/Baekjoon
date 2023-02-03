N,M=map(int,input().split())

card=list(map(int,input().split()))

result=0
for i in range(N):
    for j in range(N):
        if j!=i:
            for k in range(N):
                if k!=i and k!=j:
                    sum=card[i]+card[j]+card[k]
                    if sum<=M:
                        if sum>=result:
                            result=sum

print(result)