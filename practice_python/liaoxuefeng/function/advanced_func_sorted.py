# /usr/bin/python3
# -*- code = utf-8 -*-

## sorted

# sorted(list, key=keywords, reverse=True/False)
# keywords can be abs, str.lower (忽略大小写)
# reverse=True 为降序

foo1 = ['Grone','awd','Tricks','number']
a = sorted(foo1,key=str.lower)
print(a)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]
def by_score(t):
    return -t[1]

L2 = sorted(L, key=by_name)
print(L2)

L2 = sorted(L, key=by_score)
print(L2)
