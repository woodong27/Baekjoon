N=int(input())

i=0
while True:
    temp,sum=0,0
    if i==N:
        i=0
        break
    else:
        temp=sum=i
        while temp!=0:
            sum=sum+temp%10
            temp=temp//10
        if sum==N:
            break
    i+=1

print(i)