#! /usr/bin/env python3
# -*- coding: utf-8 -*-

str1 = 'have a nice day'
print('The upper of str1 is:',str1.upper())
print('The lower of str1 is:',str1.lower())

n = len(str1)
str2 = str1[1:len(str1)]
print('the number of letters of str1 is '+ str(n) +' and set str2 equal to the slice from the 1st index all the way to the end of str1, which is --- '+str2)
