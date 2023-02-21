from collections import deque

N,M,V=map(int,input().split())

graph=[[0 for _ in range(N+1)]for _ in range(N+1)]

for i in range(M):
    v1,v2=map(int,input().split())
    graph[v1][v2]=1
    graph[v2][v1]=1

def dfs(start):
    visited=[]
    stack=[]
    stack.append(start)
    while stack:
        node=stack.pop()
        if node not in visited:
            visited.append(node)
            for i in range(N,0,-1):
                if graph[node][i]==1:
                    stack.append(i)

    return visited

def bfs(start):
    visited=[]
    que=deque([])
    que.append(start)
    while que:
        node=que.popleft()
        if node not in visited:
            visited.append(node)
            for i in range(1,N+1):
                if graph[node][i]==1:
                    que.append(i)

    return visited

print(*dfs(V))
print(*bfs(V))