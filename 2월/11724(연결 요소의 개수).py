V,E=map(int,input().split())

visited=[1]+[0]*V

graph=[[]for _ in range(V+1)]

for i in range(E):
    v1,v2=map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(graph,start):
    global visited
    stack=[]
    stack.append(start)

    while stack:
        now=stack.pop()
        if visited[now]==0:
            visited[now]=1
            stack.extend(graph[now])

cnt=0
while 0 in visited:
    start=visited.index(0)
    dfs(graph,start)
    cnt+=1

print(cnt)