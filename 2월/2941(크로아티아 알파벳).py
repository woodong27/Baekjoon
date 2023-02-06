word=input()

croatian=['c=','c-','dz=','d-','lj','nj','s=','z=']

count=0
for i in croatian:
    if i in word:
        while i in word:
            count+=1
            word=word.replace(i,' ',1)

word=word.replace(' ','')
print(count+len(word))