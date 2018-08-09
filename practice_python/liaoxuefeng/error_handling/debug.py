# /usr/bin/python3
# -*- code = utf-8 -*-

## debug

# 

# 1. assert
# 格式：assert 表达式(which should be true) 错误信息
# 如果断言失败，assert语句本身就会抛出AssertionError
# 程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert，这样可以把assert当作pass对待。
print('1. assert ...')
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

try:
    foo('0')
except Exception as e:
    print(e)

# 2. logging
# logging的好处：它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息
# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。

print('2. logging ...')
import logging
# logging.basicConfig(level=logging.INFO)  # set loggin level
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

# 3. pdb （单步调试）
# 使用方法：python -m pdb err.py
# 以及各种终端命令，但我觉得没必要学这个，用IDE就好
