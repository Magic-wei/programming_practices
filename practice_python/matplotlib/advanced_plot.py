#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np # for easy generation of arrays
import matplotlib.pyplot as plt
import matplotlib as mpl

from pylab import *
import matplotlib.gridspec as gridspec

# tips: use figure() or figure(n) to create a new figure.
# when you execute

# customize style
# plt.style.use('ggplot')

# customize color
green_lv1 = list(np.array([229, 245, 249]) / 255.0)
green_lv2 = list(np.array([153, 216, 201]) / 255.0)
green_lv3 = list(np.array([44, 162, 95]) / 255.0)
gray_lv3 = list(np.array([99, 99, 99]) / 255.0)

# customize plot
plt.figure(num=1, figsize=(8,5), dpi=150, facecolor=green_lv1, 
	edgecolor=gray_lv3, frameon=False)
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.subplot(2,1,1)
plt.plot(X, C, color=green_lv2, linewidth=2.5, linestyle="-", label='cosine')
plt.plot(X, S, color=green_lv3, linewidth=2.5, linestyle="-", label='sine')
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
plt.yticks([-1, 0, 1])
plt.ylabel('y')
plt.title('legends and ticks')
plt.legend()
plt.subplot(2,1,2)
line_1, = plt.plot(X, C, color=green_lv2, linewidth=2.5, linestyle="-", label='cosine')
line_2, = plt.plot(X, S, color=green_lv3, linewidth=2.5, linestyle="-", label='sine')
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, 1], [r'$-1$', r'$0$', r'$+1$'])
plt.xlabel('x')
plt.ylabel('y')
plt.legend([line_1, line_2], ['Line 1','Line 2'], loc='lower left', bbox_to_anchor=[0.5,0.], 
	frameon=False, ncol=2)
ax = gca()
ax.set_xlim(-np.pi, np.pi)
ax.set_ylim(-1, 1)

figure()
line_3, = plt.plot(X, C, color=green_lv2, linewidth=2.5, linestyle="-", label='cosine')
line_4, = plt.plot(X, S, color=green_lv3, linewidth=2.5, linestyle="-", label='sine')
first_legend = plt.legend([line_3], loc=1)
ax = plt.gca().add_artist(first_legend)
plt.legend(handles=[line_4],loc=4)
# see [legend](https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.legend)

# Transform in axes coordinates
fig = plt.figure()
for i, label in enumerate(('A', 'B', 'C', 'D')):
    ax = fig.add_subplot(2,2,i+1)
    ax.text(0.05, 0.95, label, transform=ax.transAxes,
      fontsize=16, fontweight='bold', va='top')

# Transform in data coordinates
x = np.arange(0, 10, 0.005)
y = np.exp(-x/2.) * np.sin(2*np.pi*x)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)
ax = fig.add_subplot(335)

# advanced subplot using gridspec
figure()
G = gridspec.GridSpec(3, 3)
axes_1 = subplot(G[0, :])
xticks([]), yticks([])
text(0.5,0.5, 'Axes 1',ha='center',va='center',size=24,alpha=.5)

axes_2 = subplot(G[1,:-1])
xticks([]), yticks([])
text(0.5,0.5, 'Axes 2',ha='center',va='center',size=24,alpha=.5)

axes_3 = subplot(G[1:, -1])
xticks([]), yticks([])
text(0.5,0.5, 'Axes 3',ha='center',va='center',size=24,alpha=.5)

axes_4 = subplot(G[-1,0])
xticks([]), yticks([])
text(0.5,0.5, 'Axes 4',ha='center',va='center',size=24,alpha=.5)

axes_5 = subplot(G[-1,-2])
xticks([]), yticks([])
text(0.5,0.5, 'Axes 5',ha='center',va='center',size=24,alpha=.5)

# Axes - any location in the figure
figure(3)
axes([0.1,0.1,.8,.8])
xticks([]), yticks([])
text(0.6,0.6, 'axes([0.1,0.1,.8,.8])',ha='center',va='center',size=20,alpha=.5)

axes([0.2,0.2,.3,.3])
xticks([]), yticks([])
text(0.5,0.5, 'axes([0.2,0.2,.3,.3])',ha='center',va='center',size=16,alpha=.5)

# plt.savefig("images/axes.png",dpi=64)

# 
axes([0.1,0.1,.5,.5])
xticks([]), yticks([])
text(0.1,0.1, 'axes([0.1,0.1,.5,.5])',ha='left',va='center',size=16,alpha=.5)

axes([0.2,0.2,.5,.5])
xticks([]), yticks([])
text(0.1,0.1, 'axes([0.2,0.2,.5,.5])',ha='left',va='center',size=16,alpha=.5)

axes([0.3,0.3,.5,.5])
xticks([]), yticks([])
text(0.1,0.1, 'axes([0.3,0.3,.5,.5])',ha='left',va='center',size=16,alpha=.5)

axes([0.4,0.4,.5,.5])
xticks([]), yticks([])
text(0.1,0.1, 'axes([0.4,0.4,.5,.5])',ha='left',va='center',size=16,alpha=.5)

# Annotating Axes
# [annotations_guide](https://matplotlib.org/users/annotations_guide.html)
# see <connectionstyle_demo.py> and <annotate_explain.py>


# Equations
eqs = []
eqs.append((r"$e^{i\pi} + 1 = 0$"))
eqs.append((r"$\frac{d\rho}{d t} + \rho \vec{v}\cdot\nabla\vec{v} = -\nabla p + \mu\nabla^2 \vec{v} + \rho \vec{g}$"))
eqs.append((r"$\int_{-\infty}^\infty e^{-x^2}dx=\sqrt{\pi}$"))
eqs.append((r"$E = mc^2 = \sqrt{{m_0}^2c^4 + p^2c^2}$"))
eqs.append((r"$F_G = G\frac{m_1m_2}{r^2}$"))


plt.axes([0.025,0.025,0.95,0.95])

for i in range(24):
    index = np.random.randint(0,len(eqs))
    eq = eqs[index]
    size = np.random.uniform(12,32)
    x,y = np.random.uniform(0,1,2)
    alpha = np.random.uniform(0.25,.75)
    plt.text(x, y, eq, ha='center', va='center', color=list(np.array([17, 85, 124]) / 255.0), alpha=alpha,
             transform=plt.gca().transAxes, fontsize=size, clip_on=True)

plt.xticks([]), plt.yticks([])

plt.show()