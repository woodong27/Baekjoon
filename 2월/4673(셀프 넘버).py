def d(n):
    result=n
    while n!=0:
        result+=n%10
        n=n//10

    return result

lst=[d(x) for x in range(1,10001)]

for i in range(1,10001):
    if i not in lst:
        print(i)