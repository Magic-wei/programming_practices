# /usr/bin/python3
# -*- code = utf-8 -*-

## class information

# type, isinstance, dir

# 1. type
class animal(object):
    pass
class dog(animal):
    pass

a = animal()
d = dog()

print(type(123))
print(type([1,4,'a']))
print('str\'s type is ',type(str))
print(type(a))
print('animal\'s type is ',type(animal))

## you can also judge if two types are the same
print(type(123)==int)
print(type('str')==str)
print(type(d)==animal) # type cannot find the relationship between a class and its derivatives.

## how to judge if a object is a function? like this:
import types
def fn():
    pass

print(type(fn)) # it is a function class ...
print(type(abs))
print(type(lambda x:x))
print(type((x for x in range(10))))
print(type([x for x in range(10)]))

print(type(fn) == types.FunctionType)
print('Is abs a FunctionType? ',type(abs) == types.FunctionType)
print('Is abs a BuiltinFunctionType? ',type(abs) == types.BuiltinFunctionType)
print('Is lambda x:x a FunctionType? ',type(lambda x:x) == types.FunctionType)
print('Is lambda x:x a LambdaType? ',type(lambda x:x) == types.LambdaType)
print('Is (x for x in range(10)) a GeneratorType? ',type((x for x in range(10))) == types.GeneratorType)

# 2. isinstance
## isinstance is better than type, because it can find the relationship between a class and its derivatives, and more flexible.

print(isinstance(d,animal))
print(isinstance(d,dog))
## isinstance can also be used to find whether it is one of several types
print(isinstance([1, 2, 3], (list, tuple))) 

# 3. dir
## the most powerful function which can track all methods of a class
print('all methods of "ABC", the string class, are: ',dir('ABC'))

class Myobject(object):
    def __init__(self,x):
        self.x = x
    def power(self):
        return self.x * self.x

obj = Myobject(8)

# then, we can test its properties:
print(hasattr(obj, 'x') ) # have attribute 'x'?
print(hasattr(obj, 'y') ) # have attribute 'y'?
setattr(obj, 'y', 19) # set an attribute 'y'
print(hasattr(obj, 'y') ) # have attribute 'y'?
print(getattr(obj, 'y') ) # get the value of attribute 'y'
print(getattr(obj, 'z', 404)) # if we get a nonexistent attribute 'z', we will get AttributeError, but we can set a default return value 404 when this kind of error arises. If don't, you will get AttributeError returned.

## we can also use dir() function to get information of methods in a class:
print(hasattr(obj, 'power')) # have method 'power'?

## the right way to use these function is like following example:
def readImage(fp):
    if hasattr(fp, 'read'): # if fp have method 'read()', you can use it, or you cannot use it.
        return read(fp)
    return None

print(readImage(obj))


