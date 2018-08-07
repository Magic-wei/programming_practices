# /usr/bin/python3
# -*- code = utf-8 -*-

## partial function

# 方法：一些函数有默认参数值，如果我们需要修改某些默认参数值并频繁使用，可以考虑将这个调用赋值给一个新的函数变量进行调用

# int 按照特定的进制赋值转换
a1 = int('12345')
a2 = int('12345',base=8) # 8进制，因此前面的字符串中只能出现7以下的数字
b = int('10010',base=2) # 2进制，因此前面的字符串只能出现1,0
print(a1,a2,b)
# 当然你可以通过函数定义的方式来实现：

def int2(x,base=2):
    return int(x, base)

b2 = int2('10010')
print(b2)
# 也可以使用 builtin function:
import functools
int2 = functools.partial(int, base=2)
c = int2('1000101')
print(c)
