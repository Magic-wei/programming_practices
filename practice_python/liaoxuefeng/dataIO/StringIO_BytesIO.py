# /usr/bin/python3
# -*- code = utf-8 -*-

## StringIO and BytesIO

# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。

# 1. StringIO

from io import StringIO

f = StringIO()
print(f.write('hello'))
print(f.write(' '))
print(f.write('world!'))
print(f.getvalue()) # get written string

f.write('\nHaha\nmy name is xxxx.')
print(f.getvalue())

f1 = StringIO('my name is\nxxxx')
# f1.write(' akomon awd awdawd awd') # if you use write() function, you cannot use read() function to read characters of the string. You can only init it and then use read() function.
print('use getvalue() function:\n', f1.getvalue())
print('use readline() function:')
while True:
    s = f1.readline()
    if s == '':
        break
    print(s.strip())

# 2. BytesIO

from io import BytesIO

f2 = BytesIO()
print(f2.write('中文'.encode('utf-8'))) # 写入的不是str，而是经过UTF-8编码的bytes
print(f2.getvalue())

f3 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f3.read()) # you can also use read() function, but only for init BytesIO


