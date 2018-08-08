# /usr/bin/python3
# -*- code = utf-8 -*-

## attribute of class and object

# Q: 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：

# 讨论区给出了两个方法，都很有参考意义：

## 方法1：
## 首先创建类实例，是怎么一个过程？代码如何知道用户创建了一个类实例? 通过百度，我们知道，一个类，如果被实例化，就会默认执行一次init()函数，那么，我们就可以在init()函数里对count属性进行累加。 那我们到底是Student.count+=1 呢？ 还是self.count+=1 ? 分析一下， self.count,是实例本身的的属性，一个实例对应一个count, 那这样是无法 统计总数的。 所以必须用类的属性，类的属性是所有实例都能共享访问的。 所以就写Student.count+=1 , 能在init()写出这个Student.count+=1,  是很不容易的，1， 首先，老师的例子，是将类属性直接写在类定义的下边，很容易让人误以为这是死格式，不能写到类中的函数里。2，对于类的实例化，是执行init函数，而不会执行类本身，所以类里边的count=0 是不会执行的，count 是不会在每次类实例化的时候，被初始为0的。3，更难的一点是，是要能理解，Student.count 的值，是存储在哪里的？在程序退出后，其值是否会被初始化？这点还需要思考。

class Student(object):
    count = 0
    def __init__(self,name):
        self.__name = name
        Student.count += 1

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

## 方法2：
class Student(object):
    count = 0
    def __init__(self,name):
        self.__name = name

    #操作一个和对象无关的变量时，最好还是使用类方法
    @classmethod  # 装饰器，区分实例方法和类方法的标志
    def plus_count(cls):
        cls.count += 1

print(type(Student.plus_count)) # plus_count is <class 'method'>
print(type(Student.__init__)) # __init__ is <class 'function'>

Student('Amy').plus_count()
Student('Micheal').plus_count()
Student('Bob').plus_count()
print('Students:', Student.count)

