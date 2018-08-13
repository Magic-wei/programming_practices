# /usr/bin/python3
# -*- code = utf-8 -*-

## serialization

# Part 1: Introduction
# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
# python提供了pickle模块实现序列化，但Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。
# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

# JSON表示的对象就是标准的JavaScript语言的对象，JSON类型与python类型对应关系为：
# {} - dict; [] - list; "string" - str; 1234.56 - int or float; true/false - True/False null - None
# JSON标准规定JSON编码是UTF-8.

# Part 2: Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。
import json
d = dict(name='Bob', age=20, score=88)
json_str = json.dumps(d) # return a string.
print('json_str: ',json_str)
# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
py_dict = json.loads(json_str) # convert a json string to python dict
print('py_dict: ',py_dict)

## json advances
# json function have some parameters to configure serialization. For a class type, we can try like this:

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('Bob', 20, 88)
# 自定义转换方式，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON
print(json.dumps(s,default=student2dict)) 

# 不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict。因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
print(json.dumps(s, default=lambda obj: obj.__dict__))

# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

print(json.loads(json_str, object_hook=dict2student))


