#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np # for easy generation of arrays
import matplotlib.pyplot as plt

# tips: use figure() or figure(n) to create a new figure.
# when you execute

# figure 1, easiest one, only y label.
plt.figure(1)
plt.plot([1,2,3,4]) 
plt.axis([0, 5, 0, 5])
plt.show()

# figure 2, different format styles of lines
plt.figure(2)
t = np.arange(0., 5., 0.2) # evenly sampled time at 200ms intervals
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^') # red dashes, blue squares and green triangles
plt.show()

# figure 3, control line properties
plt.figure(3)
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
y1, y2 = np.cos(x), np.sin(x)
plt.plot(x,y1, linewidth = 2.0)
plt.plot(x,y2, linewidth = 4.0)
plt.show()

# figure 4, Line2D format, more line properties settings
plt.figure(4)
line1, line2 = plt.plot(x, y1, x, y2)
plt.setp(line1, color='r', linewidth = 2.0) # line in red
plt.setp(line2, color='b', linewidth = 1.0) # line in blue
  # or you can do this in another format
lines = plt.plot(x, y1+1.5, x, y2-0.5)
plt.setp(lines, color='k', linewidth = 10.0) # lines in black
plt.show()
  # you can call the setp() function with a line or lines to see their line properties.
plt.setp(lines)

# figure 5, multiple figures
plt.figure(5)
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(2,1,2)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()

# figure 6, setting ticks and tick labels
plt.figure(6, figsize=(8,5), dpi=80)
plt.subplot(111)
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-")
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-")

plt.xlim(X.min()*1.1, X.max()*1.1)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
# plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.ylim(C.min()*1.1,C.max()*1.1)
plt.yticks([-1, 0, +1])
# plt.yticks([-1, 0, +1], [r'$-1$', r'$0$', r'$+1$'])
plt.show()

# figure 7, annotate simple text in figure
plt.figure(7)
np.random.seed(19680801) # don't mind what these data are, just focus on the text parts.
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
plt.xlabel('Smarts', fontsize=14,color='red')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()

