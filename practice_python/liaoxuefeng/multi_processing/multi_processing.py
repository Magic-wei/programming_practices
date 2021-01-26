# -*- coding: utf-8 -*-
# [Ref](https://www.liaoxuefeng.com/wiki/1016959663602400/1017628290184064)

import os
from multiprocessing import Process, Pool
import subprocess
import time, random

print('Process ({}) start...'.format(os.getpid()))

# Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# Windows 下写多进程需要用跨平台版本`multiprocessing`

def runProcess(name):
	print('Run child process %s (%s)...' % (name, os.getpid()))

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
    # Process
    # 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    print('Parent process %s.' % os.getpid())
    p = Process(target=runProcess, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

    # Pool
    # 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
    # 对Pool对象调用join()方法会等待所有子进程执行完毕，
    # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
    # 请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，
    # 这是因为Pool(4)最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。
    # 由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果。
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')