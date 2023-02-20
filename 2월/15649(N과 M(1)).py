N,M=map(int,input().split())

lst=[i for i in range(1,N+1)]

from itertools import permutations as perm

for i in list(perm(lst,M)):
    print(*i)