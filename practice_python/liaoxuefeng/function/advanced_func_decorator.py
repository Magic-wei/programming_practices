# /usr/bin/python3
# -*- code = utf-8 -*-

## decorator

def now(n):
    print(n)
f = now
f('something to eat')
print('function %s\'s name is %s'%('now', now.__name__))
print('function %s\'s name is %s'%('f', now.__name__))

# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
def log(func):
    def wrapper(*args, **kw): # "*args, **kw" 的写法保证可以传递任意形式的参数表
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

def log_txt(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log
def now1(n):
    print(n)

@log_txt('haha')
def now2(n):
    print(n)

now1('something to eat')
now2('something to eat')

# but ... func's name is changed!

print('function %s\'s name is %s'%('now1', now1.__name__))
print(now1)
print(now2)

# so we should copy these features to decorated function

import functools

def log_txt_wraps(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log_txt_wraps('nice')
def now3(n):
    print(n)

now3('something to eat')
