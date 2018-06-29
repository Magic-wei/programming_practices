#! /usr/bin/env python3
# -*- coding: utf-8 -*-

grade={'他':75,'她':80,'它':90}
exit=input('欢迎使用大学成绩登记查询系统！进入系统请按y，请按任意键课退出\n')
while exit=='y':
    menu=['1.录入','2.查询','3.修改','4.学生列表','5.退出']
    for features in menu:
        print(features)
    ord=int(input('请输入你想要的操作序号:'))
    if ord==1:
        user=input('请输入需要录入的姓名:')
        grade[user]=int(input('请输入成绩:'))
        print('成绩录入完成，正在返回\n')
    elif ord==2:
        user=input('请输入需要查询的学生姓名')
        if user in grade:
            print('%s的成绩为：'%user,grade[user])
            exit=input('\n查询完毕，输入y继续查询，输入n退出本系统 \n 。')
        else:
            print('查无此人，请重新输入')
            continue 
        if exit=='n':
            print('已退出系统，欢迎再次使用')
        else:
            continue
    elif ord==3:
        user=input('请输入需要进行成绩修改的学生姓名')
        if user in grade:
            grade[user]=input('请输入正确的成绩')
            exit=input('修改完毕，输入y继续查询  \n若想退出本系统请按任意键。')
            if exit=='y':
                continue
            else:
                break
        else:
            print('查无此人，请重新修改')
            continue
    elif ord==4:
        for key in grade:
            print(key)
        print('\n\n')
    elif ord==5:
        print('已退出系统，欢迎再次使用')
        break
    else:
        print('输入错误，请重新输入')
        continue
