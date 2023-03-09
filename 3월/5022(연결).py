N,M=map(int,input().split())

circuit=[[0]*(M+1) for _ in range(N+1)]

for num in range(4):
    i,j=map(int,input().split())
    circuit[i][j]=num+1

from pprint import pprint
pprint(circuit)

