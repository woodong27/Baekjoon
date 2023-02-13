N=int(input())
n=N

if N<10:
    N=N*10+N
else:
    N=(N%10)*10+(N//10+N%10)%10

count=1
while N!=n:
    if N<10:
        N=N*10+N
    else:
        N=(N%10)*10+(N//10+N%10)%10
    count+=1

print(count)