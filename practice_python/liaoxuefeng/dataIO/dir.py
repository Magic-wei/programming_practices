# /usr/bin/python3
# -*- code = utf-8 -*-

## dir

import os

print(os.name)  # return OS type, 'posix' means Linux, Unix or Mac OS X, 'nt' means Windows.
print(os.uname())  # get more info of OS, unavailable for Windows.
print(os.environ)  # get env variables, 要获取某个环境变量key的值，可以调用os.environ.get('key')

# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。
abspath = os.path.abspath('.')  # get the absolute path of curent forder
print(abspath)
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
tmp_path = os.path.join(abspath, 'testdir')
print(tmp_path)
os.mkdir(tmp_path)
os.rmdir(tmp_path)

# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：

path_name = os.path.split('/Users/michael/testdir/file.txt')
print(path_name)
path_txt = os.path.splitext('/path/to/file.txt')
print(path_txt)

os.mknod("test.txt")  # create empty file
os.rename('test.txt', 'test.py')
os.remove('test.py')

# 但是复制文件的函数居然在os模块中不存在！幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
list_dir = [x for x in os.listdir('.') if os.path.isdir(x)]
list_py = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(list_dir)
print(list_py)
