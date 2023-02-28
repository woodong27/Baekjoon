num=int(input())

lst=list(map(int,input().split()))

students=[]
for i in range(num):
    if i==0:
        students.append(i+1)
    else:
        students.insert(len(students)-lst[i],i+1)

print(*students)