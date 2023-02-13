C=int(input())
for x in range(C):
    lst=list(map(int,input().split()))
    N=lst.pop(0)
    avg=sum(lst)/N

    count=0
    for i in range(N):
        if lst[i]>avg:
            count+=1

    result=count/N*100
    print('%.3f'%result+'%')