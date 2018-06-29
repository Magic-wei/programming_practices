#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# 上面将本文件声明为utf-8编码，这样写中文时就不会导致运行报错啦～

# numeric calculation and print test
print(3+3**2)
print(1+2)
print(int(49.7+1.0))
print(10//3)
print(10/3),print(10%3)
# ^ 不是幂函数的意思！它是指按位或

# variables
sample_val=156e2;
sample_val*=0.9;
sample_val+=20;
print(sample_val)

x,y=1,2
print(x)
print(y)

# compare
print(1<2)
compare=2!=2
print(compare)

# string
welcome_message = "Hello, welcome to Udacity!"
instructor_2 = "Charlie"
print(welcome_message+' '+instructor_2)

pet_halibut = 'Why should I be tarred with the epithet "loony" merely because I have a pet halibut?'
print(pet_halibut)

salesman = '"I think you\'re an encyclopaedia salesman"'
print(salesman)

# function usage
udacity_length = len("Udacity")
print(udacity_length)

given_name = "Charlotte"
middle_names = "Hippopotamus"
family_name = "Turner"
name_length = len(given_name + " " + middle_names + " " + family_name)
driving_licence_character_limit = 28
print(name_length <= driving_licence_character_limit)

# find out variable type

print(type(5.2))
print(type("wei"*12))
print("wei"*12) # many copies of the string. 12 times here

grams_of_sugar = float("35.0")
print(grams_of_sugar)
print(type(grams_of_sugar))

# method

print("charlotte hippopotamus turner".title())
full_name = "charlotte hippopotamus turner"
print(full_name.islower())
print(13.37.is_integer())

user_ip="192.168.0.111"
url="localhost:8000"
now="20:20"
log_message = "IP address {} accessed {} at {}".format(user_ip, url, now)
print(log_message)

# liaoxuefeng tutorials
print('My name','is','Mu')
print('100 + 200 =',100+200)
name='100 + 200 =',100+200
print(name)
print(type(name))
# name=input() or name=input('please enter your name: '), input输入的为str类型，如果需要输入数字需要转换类型

a=100
if a>0:
	print(a)
else:
	print(-a)

# Multi escape character
print('\\\t\\')
print(r'\\\t\\') # or print(r"\\\t\\")

print(''' line1
line2
line3''')

print(r'''hello, \n
world''')

# bool
print(True and False,not True) # and or not

# None is a special character, which is not equal to zero that is meaningful

print("python3版本中，字符串是以Unicode编码的，因此支持多语言")
ord('A') # char to encode number
chr(25991) # encode number to char
print('\u4e2d\u6587')

# encode and decode utf-8, ascii
encode1='中文'.encode('utf-8')
decode1=encode1.decode('utf-8')
print(encode1,decode1)

decode2 = b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
print(decode2)
# 注：由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。Python对bytes类型的数据用带b前缀的单引号或双引号表示。

# format 格式化
string1='hello, %s, you have money: %f' %('John',10000)
print(string1)
string2='hello, {}, you have money: {}'.format('John',10000)
print(string2)
string3='hello, {0}, you have money: {1:.1f}'.format('John',10000)
print(string3)

# list
classmates = ['yanglei','wangwei','magic']
len(classmates)
classmates[0]
classmates[-1] # 可以用索引-1直接获取最后一个元素，-2,-3以此类推
classmates.append('sun')
classmates.pop() # 删除list末尾的元素
classmates.pop(1) # 删除索引1对应的元素
L = ['apple',123,[1,3],True] # list也可以是多种类型混合
L1 = [] # 空list
# 下面这个写法，包含了三个list元素
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0],'\n',L[1][1],'\n',L[-1][-1]) # 这样后面两个字符串开头会多个空格，因为逗号本身会产生一个空格
print(L[0][0], L[1][1], L[-1][-1], sep='\n') # 解决了上面的空格问题

# tuple 元组
# 一旦初始化元组，则不能修改，类型也被固定了
classmates1 = ('yanglei','wangwei','sun')
t = (1) # 有歧义，python默认是小括号，这里相当于t=1
t = (1,) # 定义只有一个元素的元组需要加逗号
t = ('a', 'b', ['A', 'B'])
print(t)
t[2][0]='X'
t[2][1]=1;
print(t) # 无法改变指向，但如果指向一个内部可变的元素比如list，则可以改变list内的元素。

# if 语句
age=20
if age>18:
	print('adult')
elif age>6:
	print('teenager')
else:
	print('kid')
print('if语句结束啦') # 这地方直接在终端里调试会报错，因为终端里退出判断语句或者循环语句需要多执行一次回车，但运行.py没问题

# 循环语句
## for
classmates = ['yanglei','wangwei','magic']
for name in classmates:
	print(name)

sum=0
for i in range(11): # 生成从0开始，小于11的序列
	if i%2==0:
		continue	
	print(i)	
	sum+=i
print(sum)

## while
n=11
while n>0:
	print(n)
	n-=2
	if n<5:
		break
print('END')

# dict 字典 key-value
grade = {'yanglei':80,'wangwei':90,'magic':10}
print(grade['yanglei'])
grade['magic']=100
print(grade['magic'])
find_name = 'wangwei' in grade
find_name1 = grade.get('haha') # 不存在则返回None，or grade.get('haha',-1) 不存在时返回指定值-1
grade.pop('magic') # 删除'magic'对应的key-value
grade['new']=20 # 可以直接用赋值的方式增加dict元素，或者下面的update批量方式
grade_new = {'John':70,'Lee':14,'xiaowang':70}
grade.update(grade_new)
grade.values() # 返回字典中所有的value，可以重复

# 更多内容参考：https://www.cnblogs.com/fkblogmx/p/7825805.html
# 这个通过key计算位置的算法称为哈希算法（Hash）

# set结构
s = set([1,1,2,3,4]) # set会自动合并重复的元素，无序
s.add(10)
s.add(10)
print(s)
s.remove(10)
print(s)
s1 = set(['1','wa',3])
s2 = set([1,'wa',2])
print(s1 & s2)
print(s1 | s2)

# 不可变对象的理解
L=['b','c','a']
L.sort() # list的操作是可以改变其元素的，属于可变对象
print(L)

a='abc'
b = a.replace('a','A') # 对于str类型，这里只是通过replace方法对a指向的字符串'abc'进行操作并且返回新的字符串'Abc'，但没有改变a
print('a=',a)
print('b=',b)

# function
help(abs) # use help(FUNCTION_NAME) to learn info about the function FUNCTION_NAME.
abs(-10)
l=[1,10,4,9]
max(l)
max(1,4,3)

int(10.2)
float(10)
str(1)
bool('')

hex(100) # 十进制转十六进制
# function 别名
a=abs
a(-1)

# 定义函数
# 函数没有return时，执行完毕后自动return None
# 只写return 代表 return None
def my_abs(x):
	# 首先检查输入参数的类型是否正确
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-91))

# pass语句定义空函数，让代码先运行起来
def nop():
	pass
age = 1
if age > 0:
	pass

# 返回多个值
import math
def move(x, y, step, angle=0):
	nx = x + step*math.cos(angle)
	ny = y + step*math.sin(angle)
	return nx,ny
x,y = move(100,230,50,math.pi/6)
print(x,y)
r = move(100,230,50,math.pi/6)
print(r) # 其实函数返回的是tuple类型，但可以按位置赋值给多个变量
x1,y1 = r # 同上，这种赋值是可以的

# 设置默认参数
def power(x,n=2):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s

power(2)
power(3,5)

# 默认参数的陷阱
def add_end(L=[]):
	L.append('END')
	return L

for i in range(1,4):
	print(add_end()) # 默认参数必须指向不变对象，而list类型是可变的

# 修改方法如下
def add_end(L=None):
	if L==None: # 或者写成 "if L is None:" 也可以
		L = []
	L.append('END')
	return L

for i in range(1,4):
	print(add_end())

# 可变参数
# 在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个，最终组装成tuple类型

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc([1, 2, 3])) # 但这样需要输入一个list或tuple类型

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print( calc(1,2,3) )

l=[1,2,3]
print( calc(*l) )

print( calc() ) # 还可以输入0个参数 

# 关键字参数
#位置参数与关键字参数：上面讲的都属于位置参数
# 和可变参数类似，只不过关键字参数可以把输入的关键字参数组装成dict类型
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Adam', 45, gender='M', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, **extra) # 简化写法

# 命名关键字参数
# 只检查，不限制
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

# 限制输入的关键字
# * 表示后面的是关键字的名字
def person(name, age, *, city, job):
    print(name, age, city, job)
# 这时如果输入关键字少city或者job中至少一个就会报错。
# 写 person('wawa',11,'engineer','beijing') 会报错，没有出现关键字city和job，下面的写法才允许：
person('wawa',11,job='engineer',city='beijing')

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了，但要求仍然与上面的一样
def person(name, age, *args, city='beijing', job): # 关键字也可以有默认值
    print(name, age, args, city, job)

person('wawa',11,12,32,1,job='engineer',city='beijing')
# 输出 wawa 11 (12, 32, 1) beijing engineer

# 参数组合顺序
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

# 最神奇的是通过一个tuple和dict，你也可以调用上述函数：
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw) # 返回 a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
args = (1, 2,)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw) # a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
# 所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，但也不是所有函数都能正常运行，需要具体分析

# 递归函数

def fact(n):
	if n is 1:
		return 1
	return n * fact(n-1)

fact(10)
fact(1)
# 递归函数存在栈溢出的问题，不能递归层数过多，一般来说可以通过尾递归的方法解决，但大多数编译器都没有对尾递归做优化，所以还是会存在这个问题

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


# 从函数高级特性开始，换新的python脚本文件。


