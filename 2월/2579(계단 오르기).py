N=int(input())
stair=[0]
for i in range(N):
    stair+=[int(input())]

dp=[0]*301
dp[1]=stair[1]

for i in range(2,N+1):
    dp[i]=max(dp[i-3]+stair[i-1]+stair[i],dp[i-2]+stair[i])

print(dp[N])