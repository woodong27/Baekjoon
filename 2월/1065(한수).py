N=int(input())

if N<100:
    print(N)

else:
    count=99
    for i in range(100,N+1):
        if i%10-(i//10)%10==(i//10)%10-i//100:
            count+=1
    print(count)