#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
now = datetime.now()
print("The original formula is " + str(now))

print('%02d/%02d/%04d' %(now.month, now.day, now.year))

print '%02d:%02d:%02d' % (now.hour, now.minute, now.second)

print '%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second)

