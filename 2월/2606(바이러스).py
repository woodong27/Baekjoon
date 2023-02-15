V=int(input())
E=int(input())
graph=[[]for _ in range(101)]

def dfs(graph,start):
    visited=[0]*(101)
    stack=[]
    stack.append(start)

    while stack:
        now=stack.pop()
        if visited[now]!=1:
            visited[now]=1
            stack.extend(graph[now])

    return visited

for i in range(E):
    v1,v2=map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

print(dfs(graph,1).count(1)-1)