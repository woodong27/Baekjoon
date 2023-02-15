X=int(input())

dp=[0]*(10**6+1)

for i in range(2,X+1): #연산이 가능한 모든 경우를 수행

    #-1해주는 연산
    dp[i]=dp[i-1]+1

    #3으로 나누는 연산이 가능할 때
    if i%3==0:
        dp[i]=min(dp[i],dp[i//3]+1)

    #2로 나누는 연산이 가능할 때
    if i%2==0:
        dp[i]=min(dp[i],dp[i//2]+1)

print(dp[X])
