from collections import Counter

word=input()
word=word.lower()
dic=dict(Counter(word))
va_lst=list(dic.values())
va_lst.sort()

if len(va_lst)==1:
    print(word.upper())
elif va_lst[-1]==va_lst[-2]:
    print('?')
else:
    ans=[k for k,v in dic.items() if v==max(va_lst)]
    print(ans[0].upper())