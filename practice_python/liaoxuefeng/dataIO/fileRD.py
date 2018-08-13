# /usr/bin/python3
# -*- code = utf-8 -*-

## file Read and Write

# 1. Read files

f = open('fileRD/hello.txt','r')
print(f.read())
f.close()

# if you get IOError when open a file, f.close() won't be executed. So maybe you can use 'try finally structure':

try:
    f = open('fileRD/hello.txt','r')
    print(f.read())
finally:
    print(f)
    if f:
        f.close()

# And there is a simpler writing:

with open('fileRD/hello.txt', 'r') as f:
    print(f.read())

# let's see the methods in f:
print(dir(f))

# read() function will get all the contents in a file, so if the file is too big (e.g. 10G), your RAM will be overwhelmed. You can use read(size_n) instead, which only read size_n bytes each time.
# And you can also use readline() and readlines().

f1 = open('fileRD/testlist.txt','r')
for line in f1.readlines():
    print(line.strip()) # delete '\n' at the end of each line.

# character code and decode

# ubuntu use utf-8 as the default code method. If you get some files coding by other methods, you can set code mode when open files: (and also if you get errors when decoding, you can ignore it by setting error='ignore')
with open('fileRD/gbk.txt', 'r', encoding='gbk', errors='ignore') as f:
    print(f.read())

# 2. write to files

# 你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：

for i in range(0,10):
    with open('fileRD/writetest.txt', 'w') as f:
        f.write('Write to file: Hello, world!')

# you may notice that if you use the parameter 'w', it will overwrite previous content. If you want to append something, use 'a'.

for i in range(0,10):
    with open('fileRD/writetest_append.txt', 'a') as f:
        f.write('Write to file: Hello, world!\n')
