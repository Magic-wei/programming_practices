# /usr/bin/python3
# -*- code = utf-8 -*-

## error handling

# 1. try ... except ... (finally ...)
# 如果没有错误发生，except语句块不会被执行，但是finally如果有，则一定会被执行（可以没有finally语句）

print('1. try ... except ... (finally ...): ')

def fn(n):
    print('now we will try r = 10 / %.2f'%(n))
    try:
        print('try...')
        r = 10 / n
        print('result:', r)
    except ZeroDivisionError as e:
        print('except:', e)
    finally:
        print('finally...')
    print('END')

fn(0)
fn(2)

# there are many types of error, ValueError, ZeroDivisionError ...
# Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。下例中，第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了。


try:
    print(int(' '))
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')

# Built-in Exception hierarchy: https://docs.python.org/3/library/exceptions.html#exception-hierarchy

# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用(看'2. record error'的例子)

# 2. record error
# 如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。但也可以选择在捕获错误的同时打印出来，这样能保证程序正常执行。通过配置，logging还可以把错误记录到日志文件里，方便事后排查。
print('\n2. record error: ')

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')

# 3. throw out error (抛出错误)
print('\n3. throw out error: ')
class FooError(ValueError): # 选择好错误继承关系
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s) # 使用raise抛出错误
    return 10 / n

try:
    foo('0')
except ValueError as e:
    print(e)
print('END')

# 更常用的做法是，在某个函数内捕获到错误后，输出必要提示信息后继续向上抛错误。有问题，反映给上层处理，别一个人瞒着。
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise # 就是这里，尽管有except语句，但我们只加单词'raise'可以原样抛出错误

bar()
