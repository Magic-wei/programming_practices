# /usr/bin/python3
# -*- code = utf-8 -*-

## filter

# in: func and a list, the return value of func must be boolean.
# out: an iterator

def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd,range(1,19)))) # only leave odd number (奇数)

# 用filter求素数

# 思路：
# (1) 首先得到从2开始的自然数序列，
# (2) 从2开始，2肯定是素数，把2的倍数去掉；
# (3) 取新序列的第一个数3,过滤3的倍数，以此类推……

def _odd_iter(): # infinite odd sequence
    n = 1
    while True:
        n += 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0 # 这里是返回函数的写法，将匿名函数返回

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 上述写法等效于 it = filter(lambda x: x % n > 0, it)

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break

# 回数：左读和右读都一样的数，如12321
def is_palindrome_mine(n):
    list_n = list(map(int,str(n)))
    length = len(list_n)
    return list_n == list_n[::-1]

def is_palindrome(n):
    s1 = str(n)
    s2 = s1[::-1]
    n2 = int(s2)
    return n2 == n
# 测试:
print('begin to test palindrome (回数):')
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
