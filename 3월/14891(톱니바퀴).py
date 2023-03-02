gear=[]
for i in range(4):
    temp=list(map(int,input()))
    gear.append(temp)

K=int(input())
for _ in range(K):
    num,direction=map(int,input().split())
    num-=1
    #시계방향 : insert(0,pop())
    #반시계방향 : append(pop(0))
    if direction==-1:#반시계
        if num+1<4 and gear[num][2]!=gear[num+1][6]:
            if num+2<4 and gear[num+1][2]!=gear[num+2][6]:
                if num+3<4 and gear[num+2][2]!=gear[num+3][6]:
                    gear[num+1].insert(0,gear[num+1].pop())
                    gear[num+2].append(gear[num+2].pop(0))
                    gear[num+3].insert(0,gear[num+3].pop())
                else:
                    gear[num+1].insert(0,gear[num+1].pop())
                    gear[num+2].append(gear[num+2].pop(0))
            else:
                gear[num+1].insert(0,gear[num+1].pop())

        if num-1>=0 and gear[num][6]!=gear[num-1][2]:
            if num-2>=0 and gear[num-1][6]!=gear[num-2][2]:
                if num-3>=0 and gear[num-2][6]!=gear[num-3][2]:
                    gear[num-1].insert(0,gear[num-1].pop())
                    gear[num-2].append(gear[num-2].pop(0))
                    gear[num-3].insert(0,gear[num-3].pop())
                else:
                    gear[num-1].insert(0,gear[num-1].pop())
                    gear[num-2].append(gear[num-2].pop(0))
            else:
                gear[num-1].insert(0,gear[num-1].pop())

        gear[num].append(gear[num].pop(0))

    else: #시계방향 회전
        if num+1<4 and gear[num][2]!=gear[num+1][6]:
            if num+2<4 and gear[num+1][2]!=gear[num+2][6]:
                if num+3<4 and gear[num+2][2]!=gear[num+3][6]:
                    gear[num+1].append(gear[num+1].pop(0))
                    gear[num+2].insert(0,gear[num+2].pop())
                    gear[num+3].append(gear[num+3].pop(0))
                else:
                    gear[num+1].append(gear[num+1].pop(0))
                    gear[num+2].insert(0,gear[num+2].pop())
            else:
                gear[num+1].append(gear[num+1].pop(0))

        if num-1>=0 and gear[num][6]!=gear[num-1][2]:
            if num-2>=0 and gear[num-1][6]!=gear[num-2][2]:
                if num-3>=0 and gear[num-2][6]!=gear[num-3][2]:
                    gear[num-1].append(gear[num-1].pop(0))
                    gear[num-2].insert(0,gear[num-2].pop())
                    gear[num-3].append(gear[num-3].pop(0))
                else:
                    gear[num-1].append(gear[num-1].pop(0))
                    gear[num-2].insert(0,gear[num-2].pop())
            else:
                gear[num-1].append(gear[num-1].pop(0))

        gear[num].insert(0,gear[num].pop())

ans=0
if gear[0][0]==1:
    ans+=1
if gear[1][0]==1:
    ans+=2
if gear[2][0]==1:
    ans+=4
if gear[3][0]==1:
    ans+=8

print(ans)