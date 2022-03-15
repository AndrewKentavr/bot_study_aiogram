import numpy as np
import matplotlib.pyplot as plt

# https://proproprogs.ru/modules/matplotlib-nastraivaem-format-otobrazheniya-metok-u-koordinatnyh-osey

# ------- 1

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
x = np.arange(-np.pi / 2, np.pi, 0.1)
ax.plot(x, np.sin(x))

# Убирает числовые значения по осям x и y
ax.set_xticklabels([])
ax.set_yticklabels([])

ax.grid()
plt.show()

# ------- 2

from matplotlib.ticker import NullFormatter

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
x = np.arange(-np.pi / 2, np.pi, 0.1)
ax.plot(x, np.sin(x))

ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())

ax.grid()
plt.show()

# ------- 3

from matplotlib.ticker import FuncFormatter


def formatOy(x, pos):
    return f"[{x}]" if x < 0 else f"({x})"


fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
x = np.arange(-np.pi / 2, np.pi, 0.1)
ax.plot(x, np.sin(x))

ax.yaxis.set_major_formatter(FuncFormatter(formatOy))

ax.grid()
plt.show()

# ------- 4

from matplotlib.ticker import ScalarFormatter

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
ax.plot(x, np.sinc(x) * 1e5)

# Если мы не хотим чтобы справа были большие число (Например "100_000"), то тогда мы можем переопределить значения
sf = ScalarFormatter()
sf.set_powerlimits((-4, 4))
ax.yaxis.set_major_formatter(sf)

ax.grid()
plt.show()

# ------- 5

from matplotlib.ticker import FixedFormatter, FixedLocator

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
ax.plot(x, np.sinc(x) * 1e5)

# Если мы не хотим чтобы справа были большие число (Например "100_000"), то тогда мы можем переопределить значения
ax.xaxis.set_major_locator(FixedLocator([-3, -2, -1, 0, 1, 2, 3]))
ax.xaxis.set_major_formatter(FixedFormatter(['a', 'b', 'c', 'd', 'e', 'f', 'g']))

ax.grid()
plt.show()
