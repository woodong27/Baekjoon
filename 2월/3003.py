ans=[1,1,2,2,2,8]
lst=list(map(int,input().split()))
count=[0,0,0,0,0,0]

for i in range(len(lst)):
    if lst[i]>ans[i]:
        count[i]=ans[i]-lst[i]
    elif lst[i]<ans[i]:
        count[i]=ans[i]-lst[i]

print(*count)