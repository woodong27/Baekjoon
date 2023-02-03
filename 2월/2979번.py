A,B,C=map(int,input().split())
l=[]
for i in range(3):
    x,y=map(int,input().split())
    l.append(list((int(x) for x in range(x,y+1))))

print(l)

t1,t2,t3=[],[],[]

for i in range(1,101):
    if i in l[0] and i in l[1] and i in l[2]:
        t3.append(i)
